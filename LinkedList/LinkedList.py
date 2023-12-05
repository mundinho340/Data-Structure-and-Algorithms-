from Node import Node
class LinkedList :
    def __init__(self): 
        self.head= None
        self._size=0  # size é o comprimento da lista
    def append(self, element): # a função que irá adicionar elementos na lista
        if self.head: # se existir elemento
            pointer = self.head # pointeiro recebera um nó que tera como ref o ultimo valor da lista
            while pointer.next : # enquanto existir um proximo elemento 
                pointer = pointer.next # ponteiro recebera o proximo
            pointer.next = Node(element) # adicionaremos o valor como ultimo elemento da lista
        else:
            self.head = Node(element) 
        self._size= self._size+1 
        
    def __len__(self):
        return self._size

    def getnode(self, index):
        pointer = self.head
        if pointer:
            for i in range(index):
                pointer = pointer.next
            return pointer
        else:
            raise IndexError("Erro no index")
                
    
    def __getitem__(self, index):
        pointer = self.getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("Erro no index")
    
    def __setitem__(self, index, element):
        pointer = self.getnode(index)
        if pointer :
            pointer.data = element
        else : raise IndexError("Erro de index")
        
        
    def index(self, element):
        pointer = self.head
        i =0
        while(pointer):
            if pointer.data == element:
                return i
            pointer = pointer.next
            i+=1
        raise ValueError("Erro ")   
    
    def insert(self, index, elem):
        pointer = self.getnode(index-1)
        node = Node(elem)
        if index ==0:
            self.head.next = self.head
            self.head = node
        else:
            node.next = pointer.next
            pointer.next = node
    
    def remove(self, elem):
        anceptor = self.head
        pointer = self.head.next
        
        if self.head == elem:
            self.head = self.head.next
        else:
            while(pointer):
                if pointer.data == elem:
                    anceptor.next = pointer.next
                    pointer.next = None
                anceptor = pointer
                pointer = pointer.next
                    
            
            
            
            
                
                    
        
        
            