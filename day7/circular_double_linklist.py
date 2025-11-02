class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class CDLL:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def insert_at_start(self, data):
        new = Node(data=data)
        if self.is_empty():
            new.next = new
            new.prev = new
        else:
            new.next = self.head
            new.prev = self.head.prev
            self.head.prev.next = new
            self.head.prev = new
        self.head = new

    def insert_at_last(self, data):
        new = Node(data=data)
        if self.is_empty():
            new.next = new
            new.prev = new
            self.head = new
        else:
            new.next = self.head
            new.prev = self.head.prev
            self.head.prev.next = new
            self.head.prev = new

    def search(self, data):
        temp = self.head
        if temp is None:
            return None
        while True:
            if temp.data == data:
                return temp
            temp = temp.next
            if temp == self.head:
                break
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            new = Node(data=data)
            new.next = temp.next
            new.prev = temp
            temp.next.prev = new
            temp.next = new

    def print_list(self):
        temp = self.head
        if temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
            while temp != self.head:
                print(temp.data, end=' ')
                temp = temp.next
            print()

    def delete_first(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
            else:
                self.head.prev.next = self.head.next
                self.head.next.prev = self.head.prev
                self.head = self.head.next

    def delete_last(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
            else:
                last = self.head.prev
                last.prev.next = self.head
                self.head.prev = last.prev

    def delete_data(self, data):
        if self.head is None:
            return
        temp = self.head
        while True:
            if temp.data == data:
                if temp == self.head:
                    self.delete_first()
                elif temp.next == self.head:
                    self.delete_last()
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                return
            temp = temp.next
            if temp == self.head:
                break


clist = CDLL()
clist.insert_at_start(10)
clist.insert_at_last(20)
clist.insert_at_last(30)
clist.print_list()  # 10 20 30

node = clist.search(20)
if node:
    clist.insert_after(node, 25)

clist.print_list()  # 10 20 25 30

clist.delete_data(25)
clist.print_list()  # 10 20 30
