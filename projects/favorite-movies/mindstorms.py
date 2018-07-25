import turtle

window = turtle.Screen()
window.bgcolor("red")

def draw_square():

    brad = turtle.Turtle()
    brad.shape("classic")
    brad.color("blue")
    brad.speed(3)
    for n in range(0, 36):
        for n in range(0,4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)

##def draw_circle():

##    angie = turtle.Turtle()
##    angie.shape("turtle")
##    angie.color("black")
##    angie.speed(3)
##    angie.circle(50)

##def draw_triangle():

##    tim = turtle.Turtle()
##    tim.shape("square")
##    tim.color("yellow")
##    tim.speed(4)

##    for n in range(0,2):
##        tim.forward(100) 
##        tim.left(120)
##    tim.forward(100)

draw_square()
##draw_circle()
##draw_triangle()
window.exitonclick()
