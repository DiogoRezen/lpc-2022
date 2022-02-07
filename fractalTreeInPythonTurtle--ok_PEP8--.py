from turtle import *

speed("fastest")

# turning the turtle to face upwards
rt(-90)

# the acute angle between
# the base and branch of the Y
angle = 30


# function to plot a Y
def y_tree(sz_tree, level):

    if level > 0:
        colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        pencolor(0, 255 // level, 0)

        # drawing the base
        fd(sz_tree)

        rt(angle)

        # recursive call for
        # the right subtree
        y_tree(0.8 * sz_tree, level - 1)

        pencolor(0, 255 // level, 0)

        lt(2 * angle)

        # recursive call for
        # the left subtree
        y_tree(0.8 * sz_tree, level - 1)

        pencolor(0, 255 // level, 0)

        rt(angle)
        fd(-sz_tree)


# tree of size 80 and level 7
y_tree(80, 7)
