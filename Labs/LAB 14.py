import turtle

class Point:
    def __init__(self, NUMBER):
        self.n=NUMBER
        self.BE=turtle.Turtle("turtle")
        self.BE.color("white")
        self.BE.speed(100)

    def draw(self,x,y,z):
        self.BE=turtle.Turtle()
        self.BE.penup()
        self.BE.setpos(x,y)
        self.BE.pendown()
        self.BE.up()
        self.BE.setpos(-300,300)
        self.BE.down()

        if z==0:
            self.BE.up()
            self.BE.setpos(x,y)
            self.BE.down()
            self.BE.color("white")
            self.BE.begin_fill()
            self.BE.circle(50)
            self.BE.begin_fill()
            self.BE.color("blue")
            self.BE.write("0",font=("Baskerville Old", 40, "italic"))
            self.BE.up()
            self.BE.setpos(-500,500)
            self.BE.down()

        if z==1:
            self.BE.up()
            self.BE.setpos(x,y)
            self.BE.down()
            self.BE.color("white")
            self.BE.begin_fill()
            self.BE.circle(50)
            self.BE.begin_fill()
            self.BE.color("green")
            self.BE.write("1",font=("Verdana", 40, "italic"))
            self.BE.up()
            self.BE.setpos(-500,500)
            self.BE.down()

        if z==2:
            self.BE.up()
            self.BE.setpos(x,y)
            self.BE.down()
            self.BE.color("white")
            self.BE.begin_fill()
            self.BE.circle(50)
            self.BE.begin_fill()
            self.BE.color("red")
            self.BE.write("2",font=("Verdana", 40, "italic"))
            self.BE.up()
            self.BE.setpos(-500,500)
            self.BE.down()

        if z==3:
            self.BE.up()
            self.BE.setpos(x,y)
            self.BE.down()
            self.BE.color("white")
            self.BE.begin_fill()
            self.BE.circle(50)
            self.BE.begin_fill()
            self.BE.color("brown")
            self.BE.write("3",font=("Verdana", 40, "italic"))
            self.BE.up()
            self.BE.setpos(-500,500)
            self.BE.down()

        if z==4:
            self.BE.up()
            self.BE.setpos(x,y)
            self.BE.down()
            self.BE.color("white")
            self.BE.begin_fill()
            self.BE.circle(50)
            self.BE.begin_fill()
            self.BE.color("yellow")
            self.BE.write("4",font=("Verdana", 40, "italic"))
            self.BE.up()
            self.BE.setpos(-500,500)
            self.BE.down()

        if z==5:
            self.BE.up()
            self.BE.setpos(x,y)
            self.BE.down()
            self.BE.color("white")
            self.BE.begin_fill()
            self.BE.circle(50)
            self.BE.begin_fill() 
            self.BE.color("pink")
            self.BE.write("5",font=("Verdana", 40, "bold"))
            self.BE.up()
            self.BE.setpos(-500,500)
            self.BE.down()

        if z==6:
            self.BE.up()
            self.BE.setpos(x,y)
            self.BE.down()
            self.BE.color("white")
            self.BE.begin_fill()
            self.BE.circle(50)
            self.BE.begin_fill()
            self.BE.color("dark blue")
            self.BE.write("6",font=("Verdana", 40, "bold"))
            self.BE.up()
            self.BE.setpos(-500,500)
            self.BE.down()

        if z==7:
            self.BE.up()
            self.BE.setpos(x,y)
            self.BE.down()
            self.BE.color("white")
            self.BE.begin_fill()
            self.BE.circle(50)
            self.BE.color("white")
            self.BE.begin_fill()
            
            self.BE.color("grey")
            self.BE.write("7",font=("Verdana", 40, "bold"))
            self.BE.up()
            self.BE.setpos(-500,500)
            self.BE.down()

        if z==8:
            self.BE.up()
            self.BE.setpos(x,y)
            self.BE.down()
            self.BE.color("white")
            self.BE.begin_fill()
            self.BE.circle(50)
            self.BE.begin_fill()
            self.BE.color("orange")
            self.BE.write("8",font=("Verdana", 40, "bold"))
            self.BE.up()
            self.BE.setpos(-500,500)
            self.BE.down()

        if z==9:
            self.BE.up()
            self.BE.setpos(x,y)
            self.BE.down()
            self.BE.color("white")
            self.BE.begin_fill()
            self.BE.circle(50)
            self.BE.begin_fill()
            self.BE.color("purple")
            self.BE.write("9",font=("Verdana", 40, "bold"))
            self.BE.up()
            self.BE.setpos(-500,500)
            self.BE.down()
    
            
    def printing(self):
        w=self.n
        x=-500
        y=250
        for i in xrange(7):
            s=Point(w)
            s.draw(x,y,w[i])
            x+=150

        y-=100
        
    def Sort(self):
        Array=[]
        l=self.n
        K=True
        y=250
        

        while K:
            K=False
            for j in range(len(l)-1,0,-1):
                for i in range(j):
                    c=""
                    if l[i]>l[i+1]:
                        K=True
                        l[i],l[i+1]=l[i+1],l[i]
            x=-500
            
        for i in xrange(7):
            sea=Point(l)
            sea.draw(x,y,l[i])
            x+=150

        y-=100
        
Array2=[]
for i in range(7):
    m=input()
    Array2.append(m)
b=Point(Array2)
b.printing()
BE=b.Sort()
print BE

turtle.done()
