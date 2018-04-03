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
    brad.speed(10) #change brad speed to 10
    for i in range(1,37): #replicate 36 times at 10 degrees each to make a cricle
        draw_square(brad)
        brad.right(10) #turn 10 degrees after each square

    window.exitonclick()

draw_art()
