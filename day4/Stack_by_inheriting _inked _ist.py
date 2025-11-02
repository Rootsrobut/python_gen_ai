from link_list import *

from link_list import *

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0
    def is_empty(self):
        return super().is_empty()
    def push(self, data):
        super().insert_at_start(data)
        self.item_count+=1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            self.delete_first()
            self.item_count-=1
    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            raise IndexError('stack is underflow')
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


