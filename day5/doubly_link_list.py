class Node:
    """Node for a Doubly Linked List"""
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DLLIterator:
    """Iterator class for traversing the DLL"""
    def __init__(self, head):
        self.current = head
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data


class DLL:
    """Doubly Linked List implementation"""
    def __init__(self, head=None):
        self.head = head
    def __iter__(self):
        return DLLIterator(self.head)
        
    def is_empty(self):
        return self.head is None

    def insert_at_start(self, data):
        new = Node(None, data, self.head)
        if not self.is_empty():
            self.head.prev = new
        self.head = new

    def insert_at_last(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        new = Node(temp, data, None)
        temp.next = new

    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is None:
            return
        new = Node(temp, data, temp.next)
        if temp.next is not None:
            temp.next.prev = new
        temp.next = new

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

    def delete_last(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_data(self, data):
        if self.head is None:
            return

        temp = self.head
        # Case 1: first node matches
        if temp.data == data:
            self.delete_first()
            return

        # Traverse to find node
        while temp is not None and temp.data != data:
            temp = temp.next

        # If data not found
        if temp is None:
            return

        # Case 2: last node
        if temp.next is None:
            self.delete_last()
            return

        # Case 3: middle node
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

dll = DLL()
dll.insert_at_start(10)
dll.insert_at_last(20)
dll.insert_at_last(30)
dll.insert_at_start(5)

print("List elements:")
dll.print_list()

print("\nTraversing using iterator:")
for item in dll:
    print(item, end=' ')

dll.delete_data(20)
print("\n\nAfter deleting 20:")
dll.print_list()


