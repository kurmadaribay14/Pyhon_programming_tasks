class Person:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'My name is '+self.name
class Student(Person):
    def __init__(self,name,group):
        Person.__init__(self,name)
        self.group=group
s=Student('Vasya','ENX04')
print s
