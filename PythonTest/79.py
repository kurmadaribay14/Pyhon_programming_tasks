class Point:
    pass
p1=Point()
p1.x=1
p1.y=2
p2=Point()
p2.x=2
p2.y=p1.y
p3=p2
p1.y=3
print '('+str(p3.x)+','+str(p3.y)+')'
