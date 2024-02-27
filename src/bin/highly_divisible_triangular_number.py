def is_prime(x: int):
    """6k+-1 Primality test optimized"""
    if x % 3 == 0:
        return False
    i = 5
    while i <= (x ** 0.5) + 1:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True


primes = [2, 3]


# 20 function calls in 0.027 seconds
# https://en.wikipedia.org/wiki/Divisor_function#Properties
def using_primes(divisible_limit):
    divisible_count = 0
    x = 1

    # Generate primes till max prime divisor
    for check_prime in range(primes[-1] + 2, int(divisible_limit ** 0.5), 2):
        if is_prime(check_prime):
            primes.append(check_prime)

    while divisible_count < divisible_limit:
        divisible_count = 1
        x += 1
        triangular = int(x * (x + 1) / 2)

        temp = triangular
        for prime in primes:
            if temp % prime == 0:
                c = 0
                while temp % prime == 0:
                    c += 1
                    temp = temp / prime
                divisible_count *= (c + 1)
                if temp == 1:
                    break

    return triangular


# 5 function calls in 2.822 seconds
def naive(divisble_limit):
    divisible_count = 0
    x = 1
    while divisible_count < divisble_limit:
        divisible_count = 0
        x += 1
        t = int(x * (x + 1) / 2)

        for i in range(1, int(t ** 0.5) + 1):
            if t % i == 0:
                # If divisors are equal only count 1
                if (t / i == i):
                    divisible_count += 1
                else:  # Otherwise count divisor pair
                    divisible_count += 2
    return t


# print(naive(500))
print(using_primes(500))
