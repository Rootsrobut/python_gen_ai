class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def insert_front(self, data):
        new = Node(data, None, self.front)
        if self.is_empty():
            self.rear = new
        else:
            self.front.prev = new
        self.front = new
        self.item_count += 1

    def insert_rear(self, data):
        new = Node(data, self.rear, None)
        if self.is_empty():
            self.front = new
        else:
            self.rear.next = new
        self.rear = new
        self.item_count += 1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.front.data

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.rear.data

    def size(self):
        return self.item_count


# --- Test code ---
d1 = Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.get_front(), d1.get_rear())  
d1.delete_front()
print(d1.get_front(), d1.get_rear())  
d1.delete_rear()
print(d1.get_front(), d1.get_rear())  
