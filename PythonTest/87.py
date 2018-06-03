class Student:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def __str__(self):
        return (self.name+' '+self.surname)
a=[]
s1=Student('Vasya','Pupkin')
s2=Student('John','Smit')
s3=Student('Igor','Tutkin')
a.append(s1)
a.append(s2)
a.append(s3)
print a[2]
