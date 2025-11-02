def bubblesort(list1):
    n=len(list1)
    for i in range(1,n):
        for j in range(n-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]

def modifiybubblesort(list1):
    flag=False
    n=len(list1)
    for i in range(1,n):
        flag=False
        for j in range(n-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
                flag=True
        if not flag:
            break


def selectionsort(list1):
    n=len(list1)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if list1[j]<list1[min_index]:
                min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i]        


def inserttionsort(list1):
    n=len(list1)
    for i in range(1,n):
        temp=list1[i]
        j=i-1
        while j>=0 and temp<list1[j]:
            list1[j+1]=list1[j]
            j-=1
        list1[j+1]=temp

def merge_sort(list1):
    if len(list1) > 1:                     
        mid = len(list1) // 2              
        left_half = list1[:mid]            
        right_half = list1[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list1[k] = left_half[i]
                i += 1
            else:
                list1[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            list1[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            list1[k] = right_half[j]
            j += 1
            k += 1


def quick_sort(list1):
    if len(list1)<1:
        return list1
    else:
        pivot=list1[0] 
        lesser=[x for x in list1[1:] if x<=pivot]  
        greater=[x for x in list1[1:] if x>pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater) 
    


list1=[23,45,65,43,21,12,34,43,54,56,76,67,89,9,0,1,2,34]
bubblesort(list1)
print('bubblesort    ',list1)

list1=[23,45,65,43,21,12,34,43,54,56,76,67,89,9,0,1,2,34]
modifiybubblesort(list1)
print('modifiybubblesort',list1)

list1=[23,45,65,43,21,12,34,43,54,56,76,67,89,9,0,1,2,34]
selectionsort(list1)
print('selectionsort',list1)



list1=[23,45,65,43,21,12,34,43,54,56,76,67,89,9,0,1,2,34]
inserttionsort(list1)
print('inserttionsort ',list1)


list1=[23,45,65,43,21,12,34,43,54,56,76,67,89,9,0,1,2,34]
merge_sort(list1)
print('merge_sort    ',list1)

list1=[23,45,65,43,21,12,34,43,54,56,76,67,89,9,0,1,2,34]
list1=quick_sort(list1)
print('quick_sort    ',list1)