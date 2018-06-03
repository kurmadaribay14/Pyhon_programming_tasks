class Equation:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __str__(self):
        return(str(self.a)+'x^2+'+str(self.b)+'x+'+str(self.c))
e=Equation(4,5,2)
print e
