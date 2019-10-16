class Man:
    def __init__(self):
        self.age=5
newman=Man()
print(newman.age)

class Person:
    def __init__(self,name,age):
        self.ima=name
        self.vozrast=age
    def printfunc(self):
        print("My Name is:", self.ima)
        print("My age is:", self.vozrast)
person1=Person("Atin",34)
person1.printfunc()

#adding comment for testing jenkins
