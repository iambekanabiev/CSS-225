# Bekzodbek
# 08/11/2024
# Drawing a simple car

import turtle

def draw_car():
    # Draw the body of the car
    turtle.penup()
    turtle.goto(-50, -20)  # Positioning the turtle
    turtle.pendown()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.forward(100)  # Car body length
    turtle.left(90)
    turtle.forward(20)   # Car body height
    turtle.left(90)
    turtle.forward(100)  # Car body length
    turtle.left(90)
    turtle.forward(20)   # Car body height
    turtle.left(90)
    turtle.end_fill()

    # Draw the wheels
    turtle.penup()
    turtle.goto(-40, -30)  # Position for the left wheel
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(10)       # Wheel radius
    turtle.end_fill()

    turtle.penup()
    turtle.goto(30, -30)   # Position for the right wheel
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)       # Wheel radius
    turtle.end_fill()

# Main execution
turtle.speed(1)  # Set the speed of drawing
draw_car()
turtle.hideturtle()  # Hide the turtle
turtle.done()  # Finish drawing