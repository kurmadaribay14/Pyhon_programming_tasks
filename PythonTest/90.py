class Card:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __cmp__(self,other):
        if self.a+self.b>+other.a+other.b:
            return 1
        if self.a+self.b<+other.a+other.b:
            return -1
c1=Card(1,2)
c2=Card(2,3)
print cmp(c1,c2)
