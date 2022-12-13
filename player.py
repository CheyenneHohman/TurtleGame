from turtle import Turtle 

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    # Inheritance allows us to define a class that inherits all the methods and properties (attributes) from another class
    def __init__(self):
        # the super function returns a temporary object of the superclass that allows access to all of its methods to its child class. Need not specify parent class name to access its methods. Function can be used in single & multiple inheritances 
        # Passing in the Class sets it up, the super function allows it to work. 
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.right(270) #rotates 270 degrees to face "up" towards the top of the screen 
        self.goto(STARTING_POSITION)

        #allow forward movement
    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)

    #Mark the finish line and return a Boolean 
    def crossed_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False