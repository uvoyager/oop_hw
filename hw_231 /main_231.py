import turtle
from turtle import Turtle
t = Turtle()

class Flower:
    def __init__(self, num_flowers, num_petals, col):
        self.num_flowers = num_flowers
        self.num_petals = num_petals
        self.col = col

    def draw_fl(self):
        for i in range(self.num_flowers):
            stem = Stem(i, self.num_flowers)
            leaf_pos, top_pos = stem.paint_stem()
            leaf = Leaf(leaf_pos)
            leaf.paint_leaf()
            petals = Petal(self.num_petals, self.col)
            petals.draw_many(top_pos)

class Stem:
    def __init__(self, index, total_flowers):
        self.index = index
        self.total = total_flowers
        self.top = None
        self.f_leaf = None

    def paint_stem(self):
        t.penup()
        t.goto(0, -100)
        t.pendown()
        t.pencolor("green")
        if self.total > 1:
            deg = 120 / (self.total - 1)
            angle = 150 - (self.index * deg)
        else:
            angle = 90
            
        t.setheading(angle)
        t.forward(40)
        self.f_leaf = t.pos()
        t.forward(80)
        self.top = t.pos()
        return self.f_leaf, self.top

class Petal:
    def __init__(self, num_petals, col):
        self.num_petals = num_petals
        self.col = col

    def draw_one(self):
        t.begin_fill()
        t.forward(40)
        t.left(160)
        t.forward(40)
        t.left(20)
        t.end_fill()

    def draw_many(self, position):
        t.penup()
        t.goto(position)
        t.pendown()
        t.color(self.col)
        for _ in range(self.num_petals):
            self.draw_one()
            t.left(360 / self.num_petals)

class Leaf:
    def __init__(self, position):
        self.pos = position

    def paint_leaf(self):
        t.penup()
        t.goto(self.pos)
        t.pendown()
        t.color("green")
        t.begin_fill()
        t.right(90)
        t.circle(20, 90)
        t.left(90)
        t.circle(20, 90)
        t.end_fill()
        t.setheading(0)


n = int(input('Input the number of flowers: '))
k = int(input("Input the number of petals: "))
col = input("Input the color of the flower: ")

fl = Flower(n, k, col)
fl.draw_fl()

turtle.Screen().exitonclick()

