# this is a exaple how creating one class
# Class is a blueprint for creating object

class node():
    def __init__(self, anumber):
        self.data=anumber
        self.next= None

node1 = node(7)
node2 = node(9)
node3 = node(0)

print(node1.data, node2.data, node3.data)
