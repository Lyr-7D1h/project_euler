def is_divisible(x):
    for i in range(20, 1, -1):
        if x % i != 0:
            return False
    return True


# 232790046 function calls in 80.162 seconds
def brute():
    x = 2520
    while not is_divisible(x):
        x += 1
    return x


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


# 98 function calls (43 primitive calls) in 0.000 seconds
def using_lcm():
    res = 1
    for i in range(1, 20):
        res = lcm(res, i)
    return res


# print(brute())
print(using_lcm())
