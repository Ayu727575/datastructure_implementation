class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None
class DDL:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            prev = None
            while temp:
                prev = temp
                temp = temp.next
            prev.next = new_node
            new_node.prev = prev
    def insert_after(self,prev, data):
        curr = self.head
        while curr:
            if curr.data == prev:
                break
            curr = curr.next
        if curr is None:
            print("given prev element is not present in ddl")
        else:
            new_node = Node(data)
            temp = curr.next
            temp.prv = new_node
            new_node.next = temp
            new_node.prev = curr
            curr.next = new_node
    def display(self):
        if self.head is None:
            print("empty doubly linked list")
            return
        temp = self.head
        while temp:
            print(temp.data,"->",end=" ")
            temp = temp.next
    def reverse_list(self):
        pass
my_list = DDL()
my_list.display()
my_list.insert(4)
my_list.insert(6)
my_list.insert(7)
my_list.insert(9)
my_list.insert_after(6,10)
my_list.display()

            