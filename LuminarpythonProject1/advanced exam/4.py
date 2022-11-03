class Animal:
    def __init__(self,species):
        self.s=species
    def getanimal(self):
        print(self.s)
class Dog(Animal):
    def __init__(self):
        super().__init__(species)
        self.s=species
    def getdog(self):
        print(self.s)
        print("in dog class")
d=Dog("DOG")
d.setdog()