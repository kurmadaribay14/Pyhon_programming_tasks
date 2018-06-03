class Person:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'I am '+self.name
class Student(Person):
    def __init__(self,name,group):
        Person.__init__(self,name)
        self.group=group
    def __str__(self):
        return Person.__str__(self)+' from '+self.group
s=Student("Vasya","ENX04")
print s
