import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Flappy Bird")
screen.bgcolor("skyblue")
screen.setup(width=500, height=800)
screen.tracer(0)

# Create the bird
bird = turtle.Turtle()
bird.speed(0)
bird.shape("square")
bird.color("yellow")
bird.penup()
bird.goto(-150, 0)
bird.direction = "stop"

# Create the pipes
pipes = []
pipe_heights = [200, 250, 300, 350, 400]

for i in range(3):
    pipe = turtle.Turtle()
    pipe.speed(0)
    pipe.shape("square")
    pipe.color("green")
    pipe.shapesize(stretch_wid=10, stretch_len=2)
    pipe.penup()
    pipe.goto(300 + i * 200, random.choice(pipe_heights))
    pipes.append(pipe)

# Set up gravity
gravity = 0.5

# Set up jump
def jump():
    bird.direction = "up"

screen.listen()
screen.onkey(jump, "space")

# Game loop
while True:
    screen.update()

    # Move the bird
    bird.direction = "down"
    bird.sety(bird.ycor() - gravity)

    # Move the pipes
    for pipe in pipes:
        pipe.setx(pipe.xcor() - 2)

        # Check for collision with bird
        if pipe.distance(bird) < 40 and pipe.xcor() < bird.xcor():
            screen.bgcolor("red")
            bird.color("black")
            break

        # Check if pipe is off the screen
        if pipe.xcor() < -300:
            pipe.goto(300, random.choice(pipe_heights))

    # Check for collision with ground
    if bird.ycor() < -390:
        screen.bgcolor("red")
        bird.color("black")
        break

    # Set up jump physics
    if bird.direction == "up":
        gravity = 0.5
        bird.sety(bird.ycor() + 10)
        bird.direction = "down"

    # Increase gravity
    gravity += 0.01