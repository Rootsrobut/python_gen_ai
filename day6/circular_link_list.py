class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last is None

    def insert_at_start(self, data):
        new = Node(data)
        if self.is_empty():
            new.next = new
            self.last = new
        else:
            new.next = self.last.next
            self.last.next = new

    def insert_at_last(self, data):
        new = Node(data)
        if self.is_empty():
            new.next = new
            self.last = new
        else:
            new.next = self.last.next
            self.last.next = new
            self.last = new

    def search(self, data):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp != self.last:
            if temp.data == data:
                return temp
            temp = temp.next
        if temp.data == data:
            return temp
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            new = Node(data, temp.next)
            temp.next = new
            if temp == self.last:
                self.last = new

    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.data, end=' ')
                temp = temp.next
            print(temp.data)
        else:
            print("List is empty")

    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_data(self, data):
        if not self.is_empty():
            # Single node case
            if self.last.next == self.last:
                if self.last.data == data:
                    self.last = None
            else:
                # If data is at the first node
                if self.last.next.data == data:
                    self.delete_first()
                else:
                    temp = self.last.next
                    while temp != self.last:
                        if temp.next == self.last and self.last.data == data:
                            self.delete_last()
                            break
                        if temp.next.data == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next

    def __iter__(self):
        if self.last is None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)


class CLLIterator:
    def __init__(self, start):
        self.current = start
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        if self.current == self.start:
            raise StopIteration
        return data


# --- Test the Circular Linked List ---
cll = CLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)

print("List after insertions:")
cll.print_list()

# Searching
print("\nSearching for 30:", cll.search(30))

# Deleting first and last
cll.delete_first()
print("\nAfter deleting first node:")
cll.print_list()

cll.delete_last()
print("\nAfter deleting last node:")
cll.print_list()

# Deleting a specific value
cll.delete_data(30)
print("\nAfter deleting node with data 30:")
cll.print_list()
