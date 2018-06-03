class Animal:
    def __init__(self,name,which,voice,person):
        self.name=name
        self.which=which
        self.voice=voice
        self.person=person
    def getMyPerson():
        return self.person

a=[]
a1=Animal('Sharik','Dog','Gav','Shurik')
a2=Animal('Barsik','Cat','Myau','Boris')
a3=Animal('Rio','Bird','Chirik','Rid')
a4=Animal('Darvin','Hamster','Chigik','Darvin')
a.append(a1)
a.append(a2)
a.append(a3)
a.append(a4)
print a[2].getMyPerson()
