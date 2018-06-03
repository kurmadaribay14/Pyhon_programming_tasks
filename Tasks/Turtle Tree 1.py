import turtle

t = turtle.Turtle()


def x(length = 100):

    if length < 10:
        return
    t.forward(length)
    t.left(30)
    x(length *.7)
    t.right(60)
    x(length * .7)
    t.left(30)
    t.backward(length)
    return


x()

turtle.done()
