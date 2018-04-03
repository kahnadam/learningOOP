import turtle

def draw_art():
    window = turtle.Screen() #make a window
    window.bgcolor("green") #window color is green

    #make Brad
    brad = turtle.Turtle() #create an instance of a class called turtle
    brad.shape("arrow") #make brad turtle shaped
    brad.color("black") #make brad yellow
    brad.speed(5) #change brad speed to 5

    #make A
    brad.left(45)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(180)
    brad.forward(50)
    brad.left(45)
    brad.forward(70)

    #move over
    brad.penup()
    brad.goto(190,0)
    brad.pendown()

    #make K
    brad.right(90)
    brad.forward(70)
    brad.right(180)
    brad.forward(35)
    brad.left(135)
    brad.forward(49)
    brad.right(180)
    brad.forward(49)
    brad.left(90)
    brad.forward(49)
    
    window.exitonclick()

draw_art()
