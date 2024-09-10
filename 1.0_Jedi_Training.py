'''
1.0 Jedi Training (17pts)  Name: Ian Gage


1. Define Forking (1pt): 
making a copy from an organisation
2. Define Cloning (1pt): 
creating a copy of a specific repository or branch within a repository
3. Define Branching (1pt):
diverting from a main project to test different aspects of a project
4. Define Committing (1pt): 
marking a hard save, a snapshot of code
5. Define Merging (1pt): 
combining a testing branch and main branch together in the master branch
6. Define Pushing (1pt):
the way of taking code from a project into your repo
7. Define Pull Request (1pt):
it's the way of transferring  code from one repo to another

8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle

tina = turtle.Turtle()
tommy = turtle.Turtle()

tina.speed(10)
tommy.speed(10)

tina.color('black')
tommy.color('white')

tina.shape('turtle')
tommy.shape('turtle')

tina.ht()
tommy.ht()


tina.begin_fill() #black background
tina.goto(-200,0)
tina.goto(-200,200)
tina.goto(200,200)
tina.goto(200,-200)
tina.goto(-200,-200)
tina.goto(-200,0)

tina.end_fill()

tommy.penup() #just to move the turtle into position
tommy.goto(-160,-75)
tommy.pendown()


tommy.color("#fcaf51")
tommy.begin_fill() #TF|2 logo time
tommy.goto(-50, 150)
tommy.goto(0, 150)
tommy.goto(115, -75)
tommy.goto(5, -75)
tommy.goto(-45,-25)
tommy.goto(35,-25)
tommy.goto(-25, 100)
tommy.goto(-110, -75)
tommy.goto(-160,-75)
tommy.end_fill()

tommy.penup() #just to move the turtle into position
tommy.goto(-115,-75)
tommy.pendown()

tommy.color("cyan")
tommy.begin_fill() #TF|2 logo time
tommy.goto(0, 150)
tommy.goto(50, 150)
tommy.goto(160, -75)
tommy.goto(45, -75)
tommy.goto(5,-25)
tommy.goto(85,-25)
tommy.goto(25, 100)
tommy.goto(-60, -75)
tommy.goto(-115,-75)
tommy.end_fill()

tommy.penup() #just to move the turtle into position
tommy.goto(-135,-75)
tommy.pendown()


tommy.color("white")
tommy.begin_fill() #TF|2 logo time
tommy.goto(-25, 150)
tommy.goto(25, 150)
tommy.goto(135, -75)
tommy.goto(20, -75)
tommy.goto(-20,-25)
tommy.goto(60,-25)
tommy.goto(0, 100)
tommy.goto(-85, -75)
tommy.goto(-135,-75)
tommy.end_fill()

tommy.penup() #name
tommy.goto(-135, -120)
tommy.write('Ian Gage',font=("Arial", 12, "normal"))

turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
