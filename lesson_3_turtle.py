import turtle

def draw_square():
    window = turtle.Screen() #make a window
    window.bgcolor("red") #window color is red
    
    brad = turtle.Turtle() #define brad as the turtle

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