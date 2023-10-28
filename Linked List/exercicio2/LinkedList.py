from Node import Node

class LinkedList : 
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, elem):
        pointer = self.head
        if pointer:
            while pointer.next:
                pointer = pointer.next 
            pointer.next= Node(elem)
        else:
            self.head = Node(elem)
        self._size = self._size+1
    
    def __len__(self):
        return  self._size
    
    def index(self , elem):
        pointer = self.head
        i=0
        while (pointer):
            if pointer.data == elem:
                return i
            i+=1
            pointer= pointer.next
        raise IndexError("Erro ao encontrar o valor")
    
    def getNode(self, index):
        pointer = self.head 
        if pointer:
            for i in range(index):
                pointer = pointer.next
                pointer
            return pointer
       
                
        
    
    def __getitem__(self, index):
        pointer = self.getNode(index)
        if pointer:
            pointer = pointer.data
            return pointer
        else:
            raise IndexError("Erro no indice")
    
    def __setitem__(self, index, elem):
        pointer = self.getNode(index)
        if pointer:
            node = Node(elem)
            pointer.data = node.data
        else :
            raise IndexError("Erro no indice")
        
    def insert(self, index, elem):
        pointer = self.getNode(index-1)
        node = Node(elem)
        if index ==0:
            node.next = self.head
            self.head =node
        else:
            node.next= pointer.next
            pointer.next = node
            
    def remove(self , elem):
        pointer= self.head
        if self.head.data == elem:
            self.head = self.head.next
        else:
            ancesor = pointer
            while(pointer)
    
            
        
        
        
            
            
            
        

                                      