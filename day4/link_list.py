class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class SLL:
    def __init__(self,head=None):
        self.head=head
    def is_empty(self):
        return self.head==None 
    def insert_at_start(self,data):
        new=Node(data,self.head)
        self.head=new   
    def insert_at_last(self,data):
        new=Node(data)
        if not self.is_empty():
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new
        else:
            self.head=new   
    def search(self,data):
        temp=self.head
        while temp is not None:
            if temp.data==data:
                return temp
            temp=temp.next
        return None                
    def insert_after(self,temp,data):
        if temp is not None:
            new=Node(data,temp.next)
            temp.next=new  
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=' ') 
            temp=temp.next
    def delete_first(self):
        if self.head is not None:
            self.head=self.head.next
    def delete_last(self):
        if self.head is None:
            pass
        elif self.head.next is not None:
            self.head=None
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def delete_data(self,data):
        if self.head is None:
            pass
        elif self.head.next is None:
            if self.head.data==data:
                self.head=None
        else:
            temp=self.head
            if temp.data==data:
                self.head=temp.next
            else:
                while temp.next is not None:
                    if temp.next.data==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        return SLLIterator(self.head)                    

class SLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        return data            

if __name__ == "__main__":
    mylist=SLL()
    mylist.insert_at_start(20)
    mylist.insert_at_start(10)
    mylist.insert_at_last(30)
    mylist.insert_after(mylist.search(20),25)
    mylist.insert_at_last(40)
    mylist.insert_at_last(50)
    mylist.delete_data(25)
    mylist.print_list()
    print()  
    for x in mylist:
        print(x, end=' ')
