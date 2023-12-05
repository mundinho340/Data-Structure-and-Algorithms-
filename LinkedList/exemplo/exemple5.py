class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, element):
        if self.head:
            pointer = Node(self.head)
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            self.head = Node(element)

    def pegar_valor(self):
        values = []
        pointer = self.head
        while pointer:
            values.append(pointer.data)
            pointer = pointer.next
        return values

