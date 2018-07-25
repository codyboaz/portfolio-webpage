import turtle

window = turtle.Screen()

def draw_name():

    d = turtle.Turtle()
    d.color("black")
    d.speed(3)
    d.left(180)
    d.forward(40)
    for n in range(1, 3):
        d.right(90)
        d.forward(40)

    d.color("white")
    d.forward(20)

    d.color("black")
 
    for n in range(1,5):
        d.forward(40)
        d.right(90)
    d.forward(40)

    d.color("white")
    d.forward(20)

    d.color("black")
    for n in range(1,5):
        d.forward(40)
        d.right(90)
    d.forward(40)
    d.left(90)
    d.forward(40)
    d.right(180)
    d.forward(40)
    d.left(90)

    d.color("white")
    d.forward(20)

    d.color("black")
    d.right(90)
    for n in range(1, 3):
        d.forward(40)
        d.left(90)
    d.forward(40)
    d.right(180)
    d.forward(80)
    d.right(90)
    d.forward(40)
        
draw_name()
window.exitonclick()
