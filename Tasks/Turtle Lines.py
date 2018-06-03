import turtle


secondp=turtle.Turtle()

secondp.shape("turtle")

##x=-300
##y=300
x2=-300
y2=300

##p.rt(90)

secondp.speed(10)

for i in xrange(1,14):
##    p.up()
##    p.setpos(x,y)
##    p.down()
##    p.fd(600)
##    x+=50

    secondp.up()
    secondp.setpos(x2,y2)
    secondp.down()
    secondp.fd(600)
    y2-=50
    
turtle.done()
