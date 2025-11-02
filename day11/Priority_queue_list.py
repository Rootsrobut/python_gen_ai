class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, data, priority):
        index = 0
        # Insert based on priority (smaller number = higher priority)
        while index < len(self.items) and self.items[index][1] < priority:
            index += 1
        self.items.insert(index, (data, priority))
    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError('Priority Queue is Empty')
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)


# Test the class
p = PriorityQueue()
p.push('Amit', 4)
p.push('Deva', 1)
p.push('Laxmi', 0)
p.push('Puspa', 3)
p.push('Niraj', 2)
p.push('Kusma', 5)

element = p.pop()
print('first element:', element)

while not p.is_empty():
    print(p.pop())




