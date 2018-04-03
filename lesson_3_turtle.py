import turtle

def draw_square():
    window = turtle.Screen() #make a window
    window.bgcolor("red") #window color is red
    
    brad = turtle.Turtle() #define brad as the turtle
    brad.shape("turtle") #make brad turtle shaped
    brad.color("yellow") #make brad yellow
    brad.speed(2) #change brad speed to 2

    brad.forward(100) #move line forward 100
    brad.right(90) #turn 90 degrees
    brad.forward(100) #move line forward 100
    brad.right(90) #turn 90 degrees
    brad.forward(100) #move line forward 100
    brad.right(90) #turn 90 degrees
    brad.forward(100) #move line forward 100
    brad.right(90) #turn 90 degrees

    window.exitonclick() #close the window when you click on it

draw_square()
