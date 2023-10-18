from Node import Node 
class LinkedList():
    def __init__(self):
        self.head= None
        self.size =0
    def append(self, element):
        if self.head:
            pointer = Node(self.head)
            while pointer.next:
                pointer = pointer.next
            pointer.next= Node(element)   
        else :
            self.head =element
        self.size = self.size+1
            
            
    def __len__(self):
        return self._size