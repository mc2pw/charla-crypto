from random import randrange

def miller_rabin(n, k=10):
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in xrange(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in xrange(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False

    return True


def gcd(a, p):
    a0 = a
    p0 = p

    if a > p:
        x = 0
        y = 1
        s = 1
        t = 0
    else:
        x = 1
        y = 0
        s = 0
        t = 1

    while a > 1 and p > 1:
        s1 = s
        t1 = t
        s = x
        t = y
        if a > p:
            q = a/p
            x *= -q
            y *= -q
            x += s1
            y += t1
            a = a % p
        else:
            q = p/a
            x *= -q
            y *= -q
            x += s1
            y += t1
            p = p % a

    return a, p, x, y

def find_prime(bits):
    min = 6074001000 << (bits - 33)
    max = (2 << bits) - 1

    while True:
        p = randrange(min, max)
        if (miller_rabin(p)):
            return p


