from turtle import *
import random

# Setup the screen and turtle
myPen = Turtle()
myPen.shape("turtle")
myPen._tracer(0)  # Disable automatic updates to improve performance
myPen.speed(0)  # Set the speed to the fastest
myPen.hideturtle()  # Hide the turtle cursor

window = Screen()
window.bgcolor("#69D9FF")  # Light blue background
y = -140  # Starting position for the first layer

# Initialize the dictionary for ingredients with color codes
ingredients = {
    "vanilla": "#f3e5ab",
    "pistachio": "#7DFA7F",
    "raspberry": "#e30b5d",
    "strawberry": "#FF0D0D",
    "cherry": "#C20067",
    "apricot": "#FFB300",
    "lemon": "#FFFA5C",
    "kiwi": "#67F55F",
    "pineapple": "#FFFF17",
    "mango": "#FFE838",
    "mint": "#5FF5A0",
    "white chocolate": "#FFFDC4",
    "milk chocolate": "#BF671F",
    "dark chocolate": "#2A1506",
    "coffee": "#d2691e",
    "toffee": "#E35209",
    "mocha": "#93c572",
    "icing sugar": "#FFFFFF"
}

# Initialize the list of layers with colors and heights
layers = [
    ["raspberry", 30],
    ["dark chocolate", 20],
    ["milk chocolate", 40],
    ["mango", 60]
    # You can add more layers if needed
]

# Preview the content of the layers (for debugging)
print(layers)

# Function to draw a rectangle (used for cake layers and plate)
def draw_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)  # Move turtle to the starting position
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Function to add icing on top of the cake
def addIcing(turtle, icing_color, y):
    draw_rectangle(turtle, icing_color, -120, y, 240, 10)  # Add a thin icing layer at the top

# Function to add a cherry on top
def addCherry(turtle, cherry_color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)  # Position the cherry
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(cherry_color)
    turtle.circle(size)  # Draw a circle for the cherry
    turtle.end_fill()

# Let's draw the plate first
draw_rectangle(myPen, "white", -150, y-10, 300, 10)

# Iterate through each layer of the cake and draw it
for layer in layers:
    draw_rectangle(myPen, ingredients[layer[0]], -120, y, 240, layer[1])
    y += layer[1]  # Move up for the next layer

# Add icing sugar on top
addIcing(myPen, ingredients["icing sugar"], y)

# Add a cherry on top of the icing
addCherry(myPen, ingredients["cherry"], 0, y + 10, 15)

# Update the screen to show the final cake
myPen.getscreen().update()

# Keep the window open until clicked
window.exitonclick()

