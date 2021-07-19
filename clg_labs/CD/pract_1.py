import turtle
def shape(sides,angle):
    for cont in range(sides):
        turtle.fd(50)
        turtle.rt(angle)
sides=int(input("Enter hoe many sides u have to draw?"))
angle=360/sides
turtle.reset()
turtle.color("blue")
turtle.begin_fill()
shape(sides,angle)
turtle.end_fill()
