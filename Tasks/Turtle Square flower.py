from turtle import *
wn = Screen()
sarah = Turtle()
sarah.color("orange")

for outer in range(10):     #repeat 10 times
    for inner in range(4):  #repeat four times
        sarah.forward(50)
        sarah.left(90)
    sarah.left(36)          # turn left 36 degrees

wn.exitonclick()
