class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Rectangle(Point):
    def __init__(self,x1,y1,x2,y2):
        Point.__init__(self,x1,y1)
        self.x2=x2
        self.y2=y2
    def area(self):
        w=((self.y2-self.y)**2)**(1.0/2)
        h=((self.x2-self.x)**2)**(1.0/2)
        return w*h
r=Rectangle(1,2,3,4)
print r.area()

    
