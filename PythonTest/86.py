class Operator:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __str__(self):
        return (str(self.a)+'+'+str(self.b)+'+'+str(self.c))
    def __add__(self,other):
        return Operator(self.a+other.a,self.b+other.b,self.c+other.c)
    def __sub__(self,other):
        return Operator(self.a-other.a,self.b-other.b,self.c-other.c)
    def __rmul__(self,other):
        return Operator(self.a*other.a,self.b*other.b,self.c*other.c)
a=Operator(15,20,25)
b=Operator(10,15,20)
c=Operator(5,10,15)
d=Operator(2,3,1)
e=a+b-c*d
print e
