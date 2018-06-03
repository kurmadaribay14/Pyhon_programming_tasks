class Complex:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def add(self,other):
        return Complex(self.a+other.a,self.b+other.b)
    def __str__(self):
        return (str(self.a)+'x+'+str(self.b))
c1=Complex(1,2)
c2=Complex()
print c1.add(c2)
