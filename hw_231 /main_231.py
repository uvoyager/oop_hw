import turtle
from turtle import Turtle
t = Turtle()

class Flower:
    def __init__(self):
        self.stem = Stem()
        self.petals = Petals()
        self.leaf = Leaf()

    def draw(self, n):
        for i in range(1, n + 1):
            pos = self.stem.paint_stem(n, i)
            self.petals.paint_petal()
            self.leaf.paint_leaf(pos)
class Stem:
    def paint_stem(self, i):
        self.n = n
        self.i = i
        t.pendown()
        t.pencolor("green")
        deg = 180/(n+1)
        t.setheading(180-i*deg)
        t.forward(30)
        position = t.pos()
        t.forward(70)
        return position

class Petals:
    def paint_petal(self):
        t.pencolor("red")
        for i in range(7):
            t.color("red")
            t.begin_fill()
            p = t.pos()
            t.left(360/14)
            t.forward(30)
            t.right(180-14)
            t.forward(30)
            t.right(180-14)
            t.end_fill()
            t.goto(p)

class Leaf:
    def paint_leaf(self, position):
        t.pencolor('green')
        t.penup()
        t.goto(position)
        t.pendown()
        t.color("green")
        t.begin_fill()
        t.forward(40)
        t.right(160)
        t.forward(21)
        t.end_fill()
        t.penup()
        t.home()

n = int(input('Input the number: '))
a = Flower()
a.draw(n)
turtle.Screen().exitonclick()