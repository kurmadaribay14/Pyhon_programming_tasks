class Person:
    def __init__(self,name):
        self.name=name
    def _str_(self):
        return 'I am'+self.name
class Student(Person):
    def __init__(self,name,surname):
        Person.__init__(self,name)
        self.surname=surname
    def __str__(self):
        return 'My name is '+self.name+' '+self.surname
s=Student("Vasya","Pupkin")
print s
