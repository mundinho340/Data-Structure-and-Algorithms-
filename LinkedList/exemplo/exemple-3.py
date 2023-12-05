class Node():
    def __init__(self, anumber):
        self.data=anumber
        self.next= None

class LinkedList():
    def __init__(self):
        self.head = None
        
    def append (self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
    def show_elements(self): 
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

list1 = LinkedList()
list1.append(2)
list1.append(4)
list1.append(5)

