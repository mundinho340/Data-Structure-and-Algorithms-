class person :
    def __init__(self):
        self.nome= None
        self.idade=None
        

p1 = person()
p1.idade=13
p1.nome="Raimundo"


p2= person()
p2.idade= 14
p2.nome="Juice"

print(f"{p2.nome} <=> {p1.nome}")

