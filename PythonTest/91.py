class Person:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
class Student(Person):
    pass
s=Student('Vasya')
print s
                   
