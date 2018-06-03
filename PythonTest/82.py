class Student:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def __str__(self):
        return (self.name+' '+self.surname)
    def changeName(self,name):
        self.name=name
s=Student('Vasya','Pupkin')
s.changeName('Igor')
print s
