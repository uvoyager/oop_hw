from math import pi
class Triangle:
    def __init__ (self, a, b, c):
        assert int(a) > 0 and int(b) > 0 and int(c) > 0
        assert int(a)+int(b) > int(c) and int(a)+int(c) > int(b) and int(b)+int(c) > int(a)
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        p = (self.a + self.b + self.c)/2
        ar = (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
        return ar
    def __str__(self):
        return f"Triangle = {self.a, self.b, self.c}, perimeter = {self.perimeter()}, area = {self.area()}\n"

class Rectangle:
    def __init__ (self, a,b):
        assert int(a) > 0 and int(b) > 0
        self.a = int(a)
        self.b = int(b)
    def perimeter(self):
        return (self.a + self.b) * 2
    def area(self):
        return self.a * self.b
    def __str__(self):
        return f"Rectangle = {self.a, self.b}, perimeter = {self.perimeter()}, area = {self.area()}\n"

class Trapeze:
    def __init__ (self, a, b, c, d):
        assert int(a) > 0 and int(b) > 0 and int(c) > 0 and int(d) > 0 and (int(d)-int(a) < int(b) + int(c))
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = int(d)
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        p = (self.a + self.b + self.c + self.d)/2
        assert (p-self.c)*(p-self.d)*(p-self.b)*(p-self.b-self.d) > 0
        ar = ((self.a+self.b)/4*(self.a-self.b))*((p-self.c)*(p-self.d)*(p-self.b)*(p-self.b-self.d))**0.5
        return ar
    def __str__(self):
        return f"Trapeze = {self.a, self.b, self.c, self.d}, perimeter = {self.perimeter()}, area = {self.area()}\n"

class Parallelogram:
    def __init__ (self, a, b, h):
        assert int(a) > 0 and int(b) > 0 and int(h) > 0 and (int(a) > int(h) or int(b) > int(h))
        self.a = int(a)
        self.b = int(b)
        self.h = int(h)
    def perimeter(self):
        return (self.a +self.b)*2
    def area(self):
        return (self.a + self.b)/2 * self.h
    def __str__(self):
        return f"Parallelogram = {self.a, self.b, self.h}, perimeter = {self.perimeter()}, area = {self.area()}\n"


class Circle:
    def __init__ (self, r):
        assert r > 0
        self.r = int(r)
    def perimeter(self):
        return 2*pi*self.r
    def area(self):
        return pi*self.r**2
    def __str__(self):
        return f"Circle = {self.r}, length = {self.perimeter()}, area = {self.area()}\n"

    
fs = ["input01.txt", "input02.txt", "input03.txt"]
res = []
for f in fs:
    figures = []
    with open(f, "r") as l:
        lines = l.readlines()
        for ls in lines:
            line = ls.strip()
            word = line.split()
            if word[0] == "Triangle":
                a, b, c = map(int, word[1:])
                try:
                    tr = Triangle(a, b, c)
                    figures.append(tr)
                except AssertionError:
                    pass

                
            if word[0] == "Rectangle":
                a, b = map(int, word[1:])
                try:
                   rec = Rectangle(a, b)
                   figures.append(rec)
                except AssertionError:
                   pass

                
            if word[0] == "Trapeze":
                a, b, c, d = map(int, word[1:])
                try:
                    trap = Trapeze(a, b, c, d)
                    figures.append(trap)
                except AssertionError:
                    pass

                
            if word[0] == "Parallelogram":
                a, b, h = map(int, word[1:])
                try:
                    par = Parallelogram(a, b, h)
                    figures.append(par)
                except AssertionError:
                    pass

                
            if word[0] == "Circle":
                r = int(word[1])
                try:
                    circ = Circle(r)
                    figures.append(circ)
                except AssertionError:
                    pass

    a = 0
    p = 0
    figure = None
    for i in figures:
        try:
            fig_a = i.area()
            fig_p = i.perimeter()
        except AssertionError:
            continue
        if fig_a>a and fig_p>p:
            a = fig_a
            p = fig_p
            figure = i
    res.append(figure)



with open("output.txt", "w")as g:
    g.write(str(res[0]))
    g.write(str(res[1]))
    g.write(str(res[2]))




