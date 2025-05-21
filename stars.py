import turtle

star = turtle.Turtle()
star.speed(0)

# Draw the normal star
for _ in range(5):
    star.forward(150)
    star.right(144)

# Move to center and draw the upside-down star
star.penup()
star.goto(0, -50)
star.pendown()
star.left(180)  # Rotate 180 degrees to draw upside down

for _ in range(5):
    star.forward(-150)
    star.right(-144)

star.hideturtle()
turtle.done()