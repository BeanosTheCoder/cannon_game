""" Import Packages"""

from random import randrange
from turtle import *
from freegames import vector
import winsound

""" Specify the ball , the speed and the target """

ball = vector(-200, -200) # the red ball
speed = vector(0, 0) 
targets = [] # this is a list with the other balls
score=0

""" Define the functions """

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199 #left down corner
        ball.y = -199 #left down corner
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25
        winsound.PlaySound("bomb.wav", winsound.SND_ASYNC) #bomb sound

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(15, 'red')

    update()

def move():
    "Move ball (red) and targets (blue)."
    
    global score #as the score is not the input of this function
    
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13: #abs=absolute value
            targets.append(target)
        else:
            score += 10
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal")) 
    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50) #wait 50 milliseconds and run the function move

""" Write the score """
pen = Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal")) 

""" Set the background """
wn = Screen() 
wn.bgpic('colour_bg.gif')

""" Add the canon """
wn.addshape('cannon.gif')
cannon=Turtle()
cannon.penup()
cannon.goto(-200,-200)
cannon.shape('cannon.gif')
cannon.pendown()
cannon.stamp()

""" Let's play the game """
hideturtle()
up()
tracer(False)
onscreenclick(tap) # if you click on the screen you call the function tap
move()
done()