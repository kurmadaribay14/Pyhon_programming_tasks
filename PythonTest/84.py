class Length:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def __str__(self):
        return str(((self.x2-self.x1)**2+(self.y2-self.y1)**2)**(1.0/2))
l=Length(1,4,4,8)
print l
