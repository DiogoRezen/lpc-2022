# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import turtle
import math


def fibo_plot(n_iteration):
    a_side = 0
    b_side = 1
    square_a_side = a_side
    square_b_side = b_side

    # Setting the colour of the plotting pen to blue
    x_pen.pencolor("blue")

    # Drawing the first square
    x_pen.forward(b_side * factor)
    x_pen.left(90)
    x_pen.forward(b_side * factor)
    x_pen.left(90)
    x_pen.forward(b_side * factor)
    x_pen.left(90)
    x_pen.forward(b_side * factor)

    # Proceeding in the Fibonacci Series
    temp = square_b_side
    square_b_side = square_b_side + square_a_side
    square_a_side = temp

    # Drawing the rest of the squares
    for i in range(1, n_iteration):
        x_pen.backward(square_a_side * factor)
        x_pen.right(90)
        x_pen.forward(square_b_side * factor)
        x_pen.left(90)
        x_pen.forward(square_b_side * factor)
        x_pen.left(90)
        x_pen.forward(square_b_side * factor)

        # Proceeding in the Fibonacci Series
        temp = square_b_side
        square_b_side = square_b_side + square_a_side
        square_a_side = temp

    # Bringing the pen to starting point of the spiral plot
    x_pen.penup()
    x_pen.setposition(factor, 0)
    x_pen.seth(0)
    x_pen.pendown()

    # Setting the colour of the plotting pen to red
    x_pen.pencolor("red")

    # Fibonacci Spiral Plot
    x_pen.left(90)
    for i in range(n_iteration):
        print(b_side)
        fdwd = math.pi * b_side * factor / 2
        fdwd /= 90
        for j in range(90):
            x_pen.forward(fdwd)
            x_pen.left(1)
        temp = a_side
        a_side = b_side
        b_side = temp + b_side


# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
factor = 1

# Taking Input for the number of
# Iterations our Algorithm will run
n_iter = int(input("Enter the number of iterations (must be > 1): "))

# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number
if n_iter > 0:
    print("Fibonacci series for", n_iter, "elements :")
    x_pen = turtle.Turtle()
    x_pen.speed(100)
    fibo_plot(n_iter)
    turtle.done()
else:
    print("Number of iterations must be > 0")

print("End of execution")
# End of file
