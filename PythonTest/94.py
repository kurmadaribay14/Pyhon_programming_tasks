class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Line(Point):
    def __init__(self,x1,y1,x2,y2):
        Point.__init__(self,x1,y1)
        self.x2=x2
        self.y2=y2
    def length(self):
        return((self.x2-self.x)**2+(self.y2-self.y)**2)**(1.0/2)
l=Line(1,2,4,6)
print l.length()
