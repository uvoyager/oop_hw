import math
def rec_a(x):
    s = x
    k = 1
    yield s
    while True:
        k += 1
        s += (x**k)/k
        yield s

def rec_b(i):
    d = 1
    yield d
    while True:
        i += 1
        d*= 1/(i+1)
        yield d

def rec_c(n):
    d1 = 2
    d2 = 1
    if n ==1:
        yield d1
    elif n == 2:
        yield d2
    for i in range(3, n+1):
        d = 2*d2 - 3*d1
        yield d
        d1 = d2
        d2 = d

def rec_d(n):
    a1 = 0
    a2 = 1
    if n == 1:
        yield a1
    elif n  == 2:
        yield a2
    s = 0
    for k in range(3, n+1):
        a = a2 + k*a1
        s += 2**k*a
        yield s
        a1 = a2
        a2 = a

def rec_e(x):
    eps = 10**(-10)
    a = x
    s = a
    n = 1
    sign = -1
    while abs(a) >= eps:
        n += 2
        a = x**n/math.factorial(n)
        s += sign*a
        yield float(s)
        sign *= -1