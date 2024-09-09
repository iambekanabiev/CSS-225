import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Welcome to the Adventure Game")
screen.bgcolor("black")

# Create a turtle for drawing the welcome message
welcome_turtle = turtle.Turtle()
welcome_turtle.hideturtle()
welcome_turtle.color("white")
welcome_turtle.penup()
welcome_turtle.goto(0, 0)
welcome_turtle.write("Welcome to the Adventure Game!", align="center", font=("Arial", 24, "bold"))

# Keep the window open until clicked
screen.mainloop()
