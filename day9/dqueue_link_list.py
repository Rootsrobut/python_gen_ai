class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.front==None
    def enqueue(self,data):
        new=Node(data)
        if self.is_empty():
            self.front=new
        else:
            self.rear.next=new
        self.rear=new
        self.item_count+=1
    def dequeue(self):
        if self.is_empty():
            raise ImportError('Empty queue')
        elif self.front==self.rear:
                data=self.front.data
                self.front=None
                self.rear=None
                return data
        else:
            data=self.front.data
            self.front=self.front.next
            return data
        self.item_count-=1 
    def get_front(self):
        if self.is_empty():
            raise IndexError('No data in the queue')
        else:
            return self.front.data
    def get_rear(self):
        if self.is_empty():
            raise IndexError('No data in the queue')
        else:
            return self.rear.data
    def size(self):
        return self.item_count


q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.get_front(),q1.get_rear())
q1.dequeue()
print(q1.get_front(),q1.get_rear())




