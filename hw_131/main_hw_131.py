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

class Rectangle:
    def __init__ (self, a,b):
        assert int(a) > 0 and int(b) > 0
        self.a = int(a)
        self.b = int(b)
    def perimeter(self):
        return (self.a + self.b) * 2
    def area(self):
        return self.a * self.b

class Trapeze:
    def __init__ (self, a, b, c, d):
        assert int(a) > 0 and int(b) > 0 and int(c) > 0 and int(d) > 0
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

class Parallelogram:
    def __init__ (self, a, b, h):
        assert int(a) > 0 and b > 0 and h > 0
        self.a = int(a)
        self.b = int(b)
        self.h = int(h)
    def perimeter(self):
        return (self.a +self.b)*2
    def area(self):
        return (self.a + self.b)/2 * self.h


class Circle:
    def __init__ (self, r):
        self.r = int(r)
    def length(self):
        return 2*pi*self.r
    def area(self):
        return pi*self.r**2

fs = ["input01.txt", "input02.txt", "input03.txt"]
maximum_tr = None
maximum_rec = None
maximum_trap = None
maximum_par = None
maximum_c = None
for f in fs:
    with open(f, "r") as l:
        lines = l.readlines()
        for ls in lines:
            line = ls.strip()
            word = line.split()
            if word[0] == "Triangle":
                a, b, c = map(int, word[1:])
                try:
                    tr = Triangle(a, b, c)
                    maximum_tr = [tr, tr.perimeter(), tr.area()]
                    p_tr = tr.perimeter()
                    tr_ar = tr.area()
                    if p_tr > maximum_tr[1] and tr_ar > maximum_tr[2]:
                        maximum_tr = [tr, tr.perimeter(), tr.area()]
                except AssertionError:
                    pass
            if word[0] == "Rectangle":
                a, b = map(int, word[1:])
                try:
                    rect = Rectangle(a, b)
                    maximum_rec = [rect, rect.perimeter(), rect.area()]
                    p_rec = rect.perimeter()
                    ar_rec = rect.area()
                    if p_rec > maximum_rec[1] and ar_rec > maximum_rec[2]:
                        maximum_rect = [rect, rect.perimeter(), rect.area()]
                except AssertionError:
                   pass
            if word[0] == "Trapeze":
                a, b, c, d = map(int, word[1:])
                try:
                    trap = Trapeze(a, b, c, d)
                    p_trap = trap.perimeter()
                    trap_ar = trap.area()
                    maximum_trap = [trap, trap.perimeter(), trap.area()]
                    if p_trap > maximum_tr[1] and trap_ar > maximum_tr[2]:
                        maximum_tr = [trap, trap.perimeter(), trap.area()]
                except AssertionError:
                    pass
            if word[0] == "Parallelogram":
                a, b, h = map(int, word[1:])
                try:
                    par = Parallelogram(a, b, h)
                    par_p = par.perimeter()
                    par_ar = par.area()
                    maximum_par = [par, par.perimeter(), par.area()]
                    if par_p > maximum_par[1] and par_ar > maximum_par[2]:
                        maximum_par = [par, par.perimeter(), par.area()]
                except AssertionError:
                    pass
            if word[0] == "Circle":
                for r in word[1]:
                    try:
                        circ = Circle(r)
                        len_c = circ.length()
                        ar_c = circ.area()
                        maximum_c = [circ, circ.length(), circ.area()]
                        if len_c > maximum_c[1] and ar_c > maximum_c[2]:
                            maximum_c = [circ, circ.length(), circ.area()]
                    except AssertionError:
                        pass
str_tr = f"Triangle: perimeter={maximum_tr[1]}, area={maximum_tr[2]}\n"
str_rec = f"Rectangle: perimeter={maximum_rec[1]}, area={maximum_rec[2]}\n"
str_trap = f"Trapeze: perimeter={maximum_tr[1]}, area={maximum_tr[2]}\n"
str_par = f"Parallelogram: perimeter = {maximum_par[1]}, area = {maximum_par[2]}\n"
str_c = f"Circle: length = {maximum_c[1]}, area = {maximum_c[2]}\n"
with open("output.txt", "w")as g:
    g.write(str_tr)
    g.write(str_rec)
    g.write(str_trap)
    g.write(str_par)
    g.write(str_c)






