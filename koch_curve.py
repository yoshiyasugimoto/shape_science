import turtle

tur = turtle.Turtle()
tur.speed(0)

size = tur.getscreen().screensize()
tur.penup()
tur.setx(- size[1])
tur.sety(size[0] / 2)
tur.pendown()


def koch(generation, length):
    if generation == 0:
        tur.forward(length)

    else:
        koch(generation - 1, length / 3)
        tur.left(60)
        koch(generation - 1, length / 3)
        tur.right(120)
        koch(generation - 1, length / 3)
        tur.left(60)
        koch(generation - 1, length / 3)


for i in range(3):
    koch(2, size[0] * 1.5)
    tur.right(120)
