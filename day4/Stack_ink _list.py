from link_list import *

class Stack:
    def __init__(self):
        self.mylist=SLL()
        self.item_count=0
    def is_empty(self):
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            delete_element=self.mylist.head.data
            self.mylist.delete_first()
            self.item_count-=1
            return delete_element
    def peek(self):
        if not self.is_empty():
            return self.mylist.head.data
    def size(self):
        return self.item_count

s=Stack()
s.push(10)
s.push(20)
s.push(30)
print()
print('Top element is',s.peek())
delete_element=s.pop()
print('Deleted Element ',delete_element)
print('Top element is',s.peek())
print()