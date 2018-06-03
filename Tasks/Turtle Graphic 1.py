import turtle
def rect (bob):
    for i in range (4):
        bob.forward (100)
        bob.right (90)

jack = turtle.Turtle ()
jack.speed (100)
for j in range (120):
    rect (jack)
    jack.right (3)
