class Node:
    def __init__(self, item=None, priority=None, next=None):
        self.item = item
        self.priority = priority
        self.next = next

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.item_count = 0
    def is_empty(self):
        return self.item_count==0
    def push(self, data, priority):
        new = Node(data, priority)
        # If queue is empty or new node has higher priority (smaller number)
        if not self.head or priority < self.head.priority:
            new.next = self.head
            self.head = new
        else:
            temp = self.head
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            new.next = temp.next
            temp.next = new
        self.item_count += 1

    def pop(self):
        if not self.head:
            print("Queue is empty!")
            return None
        item = self.head.item
        self.head = self.head.next
        self.item_count -= 1
        return item

    def display(self):
        temp = self.head
        while temp:
            print(f"{temp.item} (priority: {temp.priority})", end=" -> ")
            temp = temp.next
        print("None")

    def count(self):
        return self.item_count               
# Test the class
p = PriorityQueue()
p.push('Amit', 4)
p.push('Deva', 1)
p.push('Laxmi', 0)
p.push('Puspa', 3)
p.push('Niraj', 2)
p.push('Kusma', 5)
p.display()

element = p.pop()
print('first element:', element)

while not p.is_empty():
    print(p.pop())
