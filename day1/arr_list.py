from array import *

a1=array('i',[23,12,34,65,78]) # integer(-,+) --> ('I','B') integer(+) --> ('i','b') # floating point('f','d')  #charater ('u')

print(a1)
print(type(a1))

for x in a1:
    print(x,end=' ')
print()    
for i in range(2,5,2): # start stop end
    print(a1[i],end=' ')
print()    
i=0
while(i<len(a1)):
    print(a1[i],end=' ')
    i+=1
print()   


a1.append(100)
print(a1)  
# Output: array('i', [23, 12, 34, 65, 78, 100])

print(a1.count(12))  
# Output: 1

a1.extend([200, 300])
print(a1)  
# Output: array('i', [23, 12, 34, 65, 78, 200, 300])



a1.fromlist([400, 500])
print(a1)  
# Output: array('i', [23, 12, 34, 65, 78, 400, 500])

print(a1.index(34))  
# Output: 2

a1.insert(2, 99)
print(a1)  
# Output: array('i', [23, 12, 99, 34, 65, 78])

a1.remove(65)
print(a1)  
# Output: array('i', [23, 12, 34, 78])

a1.reverse()
print(a1)  
# Output: array('i', [78, 34, 12, 23])

lst = a1.tolist()
print(lst)  
# Output: [23, 12, 34, 65, 78]


# pop() with no argument -> removes and returns last item
removed = a1.pop()
print(removed)   # 23
print(a1)       

# pop(i) -> removes and returns item at index i
removed2 = a1.pop(1)
print(removed2)  # 400
print(a1)        

# pop supports negative indices too (e.g., -1 is last)
last_item = a1.pop(-1)
print(last_item) # 12
print(a1)        


a1 = array('i', sorted(a1))
print(a1)

print('----------------------------------------------------list----------------------------------------------------------------------')

a1 = [23, 12, 34, 65, 78]
a1.append(46)
print(a1) # [23, 12, 34, 65, 78, 46]
a1.clear() 
print(a1) # []
a1 = [23, 12, 34, 65, 78]
print(a1.count(23)) # 1
a1.extend([59, 10])
print(a1) # [23, 12, 34, 65, 78, 59, 10]
print(a1.index(34)) # 2
a1.insert(2, 99)
print(a1) # [23, 12, 99, 34, 65, 78, 59, 10]
a1.pop()      # removes last item (10)
a1.pop(1)     # removes element at index 1
print(a1)  # [23, 99, 34, 65, 78, 59]
a1.remove(34)
print(a1) # [23, 99, 65, 78, 59]
a1.reverse()
print(a1) # [99, 78, 65, 59, 23]


## some methord is common in list and array  len(),max(),min(),sorted(

import numpy as np

a=np.array([1,2,3])
print(a)
b=np.array([[1,2,3],[10,20,30]])
print(b)
c = np.linspace(10, 50, 5, dtype=int)
print(c)



