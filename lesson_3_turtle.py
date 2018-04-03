import turtle


def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen() #make a window
    window.bgcolor("red") #window color is red

    #make Brad
    brad = turtle.Turtle() #create an instance of a class called turtle
    brad.shape("turtle") #make brad turtle shaped
    brad.color("yellow") #make brad yellow
    brad.speed(2) #change brad speed to 2
    draw_square(brad)
    #make Angie
    angie = turtle.Turtle() #make a second turtle
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()

draw_art()
