from Node import Node

class LinkedList:
    def __init__(self):
        self._size= 0
        self.head=None
        
    
    def append(self, elem):
        pointer = self.head
        if pointer:
            while pointer.next:
                pointer = pointer.next
            pointer.next= Node(elem)
        else:
            self.head = Node(elem)
        self._size = self._size +1
        
    def __len__(self):
        return self._size
    
    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                    pointer = pointer.next
            else:
                raise IndexError("Erro do index")
        return pointer
    
    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            pointer = pointer.data
            return pointer
        else:
            raise IndexError("Erro do index")
        
    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
            
        if pointer:
            pointer.data= Node(elem).data
        else:
            raise IndexError("Erro de sei la")
           
    def index(self, elem):
        pointer = self.head
        i=0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i+=1
        raise IndexError("O valor inserido ñ existe !")
    
    def insert(self, index, elem):
        pointer = self._getnode(index -1)
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node 
        else:
            node.next = pointer.next
            pointer.next = node
        self._size = self._size+1
            
    def remove(self,elem):
        ancestor = self.head
        pointer = self.head.next
        if self.head.data == elem:
            self.head = self.head.next
        else :
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next =None
                ancestor = pointer
                pointer = pointer.next
        return True
            
            
       
                
                
                
                
                
                
                
                    
       
            
        
    
            
            

            
              
        

            
        
    
    
    