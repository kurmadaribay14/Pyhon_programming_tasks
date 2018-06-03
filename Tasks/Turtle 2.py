import turtle
p=turtle.Turtle()
p.shape("turtle")

x=-300
y=300

p.rt(90)

for i in xrange(1,10):
    p.up()
    p.setpos(x,y)
    p.down()

    p.fd(600)
    x+=50
    
turtle.done()
