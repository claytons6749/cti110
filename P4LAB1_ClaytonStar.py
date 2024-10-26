#Star Clayton
#Oct.27, 2024
#P4LAB1
#Use turtle and loops to draw a square and triangle

#Import the library
import turtle

# create the turtle window and drawing object 
win = turtle.Screen()   
Bob= turtle.Turtle()    


# set turtle options

Bob.forward(5)          
Bob.pencolor("purple")
Bob.shape("turtle")


# Code to draw shapes
for side in range(4):
    Bob.forward(100)
    Bob.left(90)



# While loop that executes 3 times
sides = 3


while sides > 0:
    Bob.forward(100)
    Bob.left(120)
    sides = sides -1

    
# Wait for user to close window
win.mainloop()             

