import turtle
import time
import random

delay = 0.1  # sets a delay for the game

#Score variables
score = 0
high_score = 0


# Sets up screen.
wn = turtle.Screen()
wn.title("Snake Game by Carlos Garcia")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Stops all animation if tracer is set to 0

# Snake Head
head = turtle.Turtle()
head.speed(0)  # makes snake animation as fast as possible
head.shape("square")
head.color("yellow")
head.penup()  # Doesn't draw lines
head.goto(0, 0)  # Set in the middle of the screen
head.direction = "Stop"

# Snake food
food = turtle.Turtle()
food.speed(0)  # makes snake animation as fast as possible
food.shape("circle")
food.color("red")
food.penup()  # Doesn't draw lines
food.goto(0, 100)  # Set in the middle of the screen

segments = []  # list
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 15, "normal")) 
# Functions
def reset_score():
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 15, "normal"))
def go_up():
    if head.direction != "down": #Makes sure the snake does not go reverse directions
        head.direction = "up"

def go_down():
    if head.direction != "up": 
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():  # allows movement of the head snake
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":  # sets the down directions
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":  # sets left direction
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":  # sets right direction
        x = head.xcor()
        head.setx(x + 20)

# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for collision with the border
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"  
    #Hide/ delete segments
        for segment in segments:
            segment.goto(1000,1000) #Move segments off screen

    #Clear the segments list
        segments.clear()

    #Reset the score
        score = 0
        reset_score()



    # Check for collision with food
    if head.distance(food) < 20:
        # Move food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay -= 0.001

        #Increase the score
        score += 10
        
        if score > high_score:
            high_score = score
        reset_score()
        #reset the delay
        delay = 0.1

    # Move the segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    #Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            #Hides the segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            reset_score()
            #reset the delay
            delay = 0.1
    time.sleep(delay)

wn.mainloop()

