def linear_search(list1,data):
    for e in list1:
        if e==data:
            return list1.index(e)
    return None
    
def binary_search(list1, data, st, end):
    while st <= end:
        mid = (st + end) // 2
        if list1[mid] == data:
            return mid
        elif list1[mid] > data:
            return binary_search(list1, data, st, mid - 1)
        else:
            return binary_search(list1, data, mid + 1, end)
    return -1  
 




list1=[12,43,34,23,45,65,67,78,87,1,34,54,65,91,92,53,64,89,98]
data=34
print(linear_search(list1,data))
list1.sort()
print(binary_search(list1,data,0,len(list1)))
