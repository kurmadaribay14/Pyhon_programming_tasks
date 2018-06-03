class Point:
    pass
p1=Point()
p1.x=1
p1.y=2
p2=Point()
p2.x=1
p2.y=p1.y
p3=p2
p2.y=5
print p2==p3
