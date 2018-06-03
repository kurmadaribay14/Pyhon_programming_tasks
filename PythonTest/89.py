class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def printAB(self):
        return '('+self.a+' '+self.b+')'
class B:
    def call(self,x,y):
        a=A(x,y)
        print a.printAB()
b=B()
b.call('Name','Surname')
