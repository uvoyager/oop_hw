from math import pi, sqrt
class Figure:
    def perimeter(self):
        raise NotImplementedError()
    def square(self):
        raise NotImplementedError()
    def squareSurface(self):
        raise NotImplementedError()
    def squareBase(self):
        raise NotImplementedError()
    def height(self):
        raise NotImplementedError()
    def volume(self):
        raise NotImplementedError()
#ADD FORMULAS
class TwoDim(Figure):
    def perimeter(self):
        return "some formula for a perimeter"
    def square(self):
        return "some formula for an area"
    def squareSurface(self):
        return None
    def squareBase(self):
        return None
    def height(self):
        return None
    def volume(self):
        return  "some formula for an area"

#ADD FORMULAS
class ThreeDim(Figure):
    def perimeter(self):
        return None
    def square(self):
        return None
    def squareSurface(self):
        return "some formula for a surface area"
    def squareBase(self):
        return "some formula for a base area"
    def height(self):
        return "some formula for a height"
    def volume(self):
        return "some formula for a volume"

class Triangle(TwoDim):
    def __init__(self, a, b, c):
        assert int(a) > 0 and int(b) > 0 and int(c) > 0
        assert int(a) + int(b) > int(c) and int(a) + int(c) > int(b) and int(b) + int(c) > int(a)
        self._a = a
        self._b = b
        self._c = c
    def perimeter(self):
        return self._a + self._b + self._c
    def square(self):
        p = (self._a + self._b + self._c)/2
        return (p*(p-self._a)*(p-self._b)*(p-self._c))**0.5
    def volume(self):
        p = (self._a + self._b + self._c) / 2
        return (p * (p - self._a) * (p - self._b) * (p - self._c)) ** 0.5
    def __str__(self):
        return f"Triangle = {self._a, self._b, self._c}, volume = {self.volume()}\n"

class Rectangle(TwoDim):
    def __init__(self, a, b):
        assert int(a) > 0 and int(b) > 0
        self._a = a
        self._b = b
    def perimeter(self):
        return (self._a + self._b)*2
    def square(self):
        return self._a*self._b
    def volume(self):
        return self._a*self._b
    def __str__(self):
        return f"Rectangle = {self._a, self._b}, volume={self.volume()}\n"

class Trapeze(TwoDim):
    def __init__(self, a,b,c,d):
        assert int(a) > 0 and int(b) > 0 and int(c) > 0 and int(d) > 0 and abs(int(c) - int(d)) < abs(
            int(a) - int(b)) < int(c) + int(d)
        self._a = a
        self._b = b
        self._c = c
        self._d = d
    def perimeter(self):
        return self._a+self._b+self._c+self._d
    def square(self):
        x = ((self._c ** 2 - self._d ** 2) + (self._b - self._a) ** 2) / (2 * (self._b - self._a))
        h = (self._c ** 2 - x ** 2) ** 0.5
        return ((self._a + self._b) / 2) * h
    def volume(self):
        x = ((self._c ** 2 - self._d ** 2) + (self._b - self._a) ** 2) / (2 * (self._b - self._a))
        h = (self._c ** 2 - x ** 2) ** 0.5
        return ((self._a + self._b) / 2) * h
    def __str__(self):
        return f"Trapeze = {self._a, self._b, self._c, self._c}, volume={self.volume()}\n"

class Parallelogram(TwoDim):
    def __init__(self, a, b, h):
        assert int(a) > 0 and int(b) > 0 and int(h) > 0 and (int(a) > int(h) or int(b) > int(h))
        self._a = a
        self._b = b
        self._h = h
    def perimeter(self):
        return (self._a + self._b)*2
    def square(self):
        return self._a * self._h
    def volume(self):
        return self._a * self._h
    def __str__(self):
        return f"Parallelogram = {self._a, self._b, self._h}, volume = {self.volume()}\n"

class Circle(TwoDim):
    def __init__(self, r):
        assert r > 0
        self._r = r
    def perimeter(self):
        return 2*pi*self._r
    def square(self):
        return pi*self._r**2
    def volume(self):
        return pi * self._r ** 2
    def __str__(self):
        return f"Circle = {self._r}, volume = {self.volume()}\n"

class Sphere(Circle, ThreeDim):
    def __init__(self, r):
        super().__init__(r)
        self._r = r
    def squareSurface(self):
        return 4*pi*self._r^2
    def squareBase(self):
        return pi*self._r^2
    def height(self):
        return 2*self._r
    def volume(self):
        return 4/3*pi*self._r^3
    def __str__(self):
        return f"Sphere = {self._r}, volume = {self.volume()}\n"

class TriangularPyramid(Triangle, ThreeDim):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        assert int(h)>0
        self._h = h
    def squareSurface(self):
        sb = super().square()
        l = sqrt(self._h^2 + (1/9)*(self._a^2 - (self._a^2)/4))
        return sb + (3/2)*l*self._a
    def squareBase(self):
        return super().square()
    def height(self):
        return self._h
    def volume(self):
        return (self._h*super().square())/3
    def __str__(self):
        return f"TriangularPyramid = {self._a, self._h}, volume = {self.volume()}\n"

class QuadrangularPyramid(Rectangle, ThreeDim):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        assert int(h)>0
        self._h = h
    def squareSurface(self):
        sb = super().square()
        l = sqrt(self._h^2 - (self._a^2)/4)
        return sb + l*self._a + l*self._b
    def squareBase(self):
        return super().square()
    def height(self):
        return self._h
    def volume(self):
        return (super().square()*self._h)/3
    def __str__(self):
        return f"QuadrangularPyramid = {self._a, self._b, self._h}, volume = {self.volume()}\n"

class RectangularParallelepiped(Rectangle, ThreeDim):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        assert int(c)>0
        self._c = c
    def squareSurface(self):
        return 2*(self._a*self._b + self._a*self._c + self._b*self._c)
    def squareBase(self):
        return self._a*self._b
    def height(self):
        return self._c
    def volume(self):
        return self._a*self._b*self._c
    def __str__(self):
        return f"RectangularParallelepiped = {self._a, self._b, self._c}, volume = {self.volume()}\n"

class Cone(Circle, ThreeDim):
    def __init__(self, r, h):
        assert int(h)>0
        super().__init__(r)
        self._h = h
    def squareSurface(self):
        return pi*self._r*()*sqrt(self._h^2+self._r^2)
    def squareBase(self):
        return super().square()
    def height(self):
        return self._h
    def volume(self):
        return (self._r^2)*self._h/3*pi
    def __str__(self):
        return f"Cone = {self._r, self._h}, volume = {self.volume()}\n"

class TriangularPrism(Triangle, ThreeDim):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        assert int(h)>0
        self._h = h
    def squareSurface(self):
        return 2*super().square()+ self._a*self._h + self._b*self._h + self._c*self._h
    def squareBase(self):
        return super().square()
    def height(self):
        return self._h
    def volume(self):
        return super().square()*self._h
    def __str__(self):
        return f"TriangularPrism = {self._a, self._b, self._c, self._h}, volume = {self.volume()}\n"

fs = ["input01.txt", "input02.txt", "input03.txt"]
res = []
for f in fs:
    figures = []
    with open(f, "r") as l:
        lines = l.readlines()
        for ls in lines:
            line = ls.strip()
            word = line.split()
            if word[0] == 'Triangle':
                a, b, c = map(int, word[1:])
                try:
                    trig = Triangle(int(a), int(b), int(c))
                    figures.append(trig)
                except AssertionError:
                    pass

            if word[0] == "Rectangle":
                a, b = map(int, word[1:])
                try:
                    rec = Rectangle(int(a), int(b))
                    figures.append(rec)
                except AssertionError:
                    pass

            if word[0] == 'Trapeze':
                a, b, c, d = map(int, word[1:])
                try:
                    trap = Trapeze(int(a), int(b), int(c), int(d))
                    figures.append(trap)
                except AssertionError:
                    pass

            if word[0] == "Parallelogram":
                a, b, h = map(int, word[1:])
                try:
                    par = Parallelogram(int(a), int(b), int(h))
                    figures.append(par)
                except AssertionError:
                    pass

            if word[0] == "Circle":
                r = int(word[1])
                try:
                    c  =Circle(r)
                    figures.append(c)
                except AssertionError:
                    pass

            if word[0] == 'Sphere':
                r = int(word[1])
                try:
                    s = Sphere(r)
                    figures.append(s)
                except AssertionError:
                    pass

            if word[0] == 'TriangularPyramid':
                a, h = map(int, word[1:])
                try:
                    tp = TriangularPyramid(int(a), int(h))
                    figures.append(tp)
                except AssertionError:
                    pass

            if word[0] == 'QuadrangularPyramid':
                a, b, h = map(int, word[1:])
                try:
                    qp = QuadrangularPyramid(int(a), int(b), int(h))
                    figures.append(qp)
                except AssertionError:
                    pass

            if word[0] == 'RectangularParallelepiped':
                a, b, c = map(int, word[1:])
                try:
                    rp = RectangularParallelepiped(int(a), int(b), int(c))
                    figures.append(rp)
                except AssertionError:
                    pass

            if word[0] == 'Cone':
                r, h = map(int, word[1:])
                try:
                    c = Cone(r, h)
                    figures.append(c)
                except AssertionError:
                    pass

            if word[0] == 'TriangularPrism':
                a, b, c, h = map(int, word[1:])
                try:
                    tpr = TriangularPrism(int(a), int(b), int(c), int(h))
                    figures.append(tpr)
                except AssertionError:
                    pass
    a = 0
    figure = None
    for i in figures:
        try:
            v = i.volume()
        except AssertionError:
            continue
        if v > a:
            a = v
            figure = i
    res.append(figure)

with open("output.txt", "w")as g:
    g.write(str(res[0]))
    g.write(str(res[1]))
    g.write(str(res[2]))