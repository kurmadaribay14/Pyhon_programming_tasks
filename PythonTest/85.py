class Complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return (str(self.a)+'x+'+str(self.b))
    def __add__(self,other):
        return Complex(self.a+other.a,self.b+other.b)
a=Complex(4,5)
b=Complex(3,9)
print a+b
