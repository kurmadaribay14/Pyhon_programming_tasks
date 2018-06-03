class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Triangle(Point):
    def __init__(self,x1,y1,x2,y2):
        Point.__init__(self,x1,y1)
        self.x2=x2
        self.y2=y2
    def area(self):
        k1=((self.x2-self.x)**2)**(1.0/2)
        k2=((self.y2-self.y)**2)**(1.0/2)
        return k1*k2/2
t=Triangle(1,2,3,4)
print t.area()
