class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Stack:
    def __init__(self):
        self.head=None
        self.item_count=0
    def is_empty(self):
        return self.head==None
    def push(self,data):
        new=Node(data,self.head)
        self.head=new
        self.item_count+=1 
    def pop(self):
        if not self.is_empty():
            data=self.head.data
            self.head=self.head.next
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack is empty") 
    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            raise self.is_empty()
    def size(self):
        return self.item_count

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print('Total element in the stack= ',s1.size())
print('Top element on the stack is ',s1.peek())   
print('poped element',s1.pop())             
