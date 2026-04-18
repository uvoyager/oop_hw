class Rational():
    def __init__(self, num, den):       #itinitation of the fraction
        assert den != 0
        self.num = int(num)
        self.den = int(den)
        self.check()
    def nsd(self):            #checking the gcd of the numerator and denominator
        a = abs(self.num)
        b = abs(self.den)
        if b > a:
            a, b = b, a
        while b != 0:
            t = b
            b = a % b
            a = t
        return a
    def check(self):                 # the final fraction must be formed here
        if self.nsd() != 1:
            gcd = self.nsd()
            self.num = self.num//gcd
            self.den =  self.den//gcd
        if self.den < 0:
            self.num *= -1
            self.den *= -1
    def __add__(self, other):
        if isinstance(other, Rational):
            num = self.num*other.den + self.den*other.num
            den = self.den*other.den
            return Rational(num, den)
        elif isinstance(other, int):
            return self+Rational(other, 1)
        raise NotImplementedError
    def __str__(self):
        return f"{self.num}/{self.den}"

class RationalList():
    def __init__(self):
        self.l = []
    def add_to_list(self, num, den):
        self.l.append(Rational(num, den))
    def __getitem__(self, i):
        return self.l[i]
    def __len__(self):
        return len(self.l)
    def __add__(self, other):
        res = RationalList()
        res.l = self.l.copy()
        if isinstance(other, RationalList):
            res.l.extend(other.l)
        elif isinstance(other, Rational):
            res.l.append(other)
        elif isinstance(other, int):
            res.l.append(Rational(other, 1))
        else:
            raise NotImplementedError
        return res
    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.l.extend(other.l)
        elif isinstance(other, Rational):
            self.l.append(other)
        elif isinstance(other, int):
            self.l.append(Rational(other, 1))
        else:
            raise NotImplementedError
        return self

data = ['input01.txt', 'input02.txt', 'input03.txt']     # the data files
result = Rational(0, 1)
for file in data:
    with open (file, 'r') as f:
        for line in f:
            n = line.strip().split()
            ints = []
            for numbers in n:
                if '/' in numbers:
                    try:
                        num, den = map(int, numbers.split('/'))
                        result = result+Rational(num, den)
                    except AssertionError:
                        continue
                else:
                    ints.append(int(numbers))
            while len(ints)>=2:
                num = ints.pop(0)
                den = ints.pop(0)
                try:
                    result = result + Rational(num, den)
                except AssertionError:
                    continue
            if len(ints) == 1:
                result = result + Rational(ints[0], 1)
        print(result)
