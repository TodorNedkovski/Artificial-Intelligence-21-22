from turtle import *

t = Turtle()

def draw_branch(branch_length, angle):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(angle)
        draw_branch(branch_length - 15, angle)
        t.left(2 * angle)
        draw_branch(branch_length - 15, angle)
        t.right(angle)
        t.backward(branch_length)

#draw_branch(100, 60)

def draw_tree(trunk_length, angle):
    t.speed("fastest")
    t.left(90)
    t.up()
    t.backward(trunk_length)
    t.down()
    draw_branch(trunk_length, angle)
    done()

draw_tree(100, 20)
done()