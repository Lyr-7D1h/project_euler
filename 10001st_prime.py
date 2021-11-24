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


# 52385 function calls in 0.122 seconds
def get_prime_in_position(x):
    """Checks for all odd numbers if they are prime and will stop untill position x has been reached."""
    prime = 2
    check = 3
    pos = 1
    while pos < x + 1:
        if is_prime(check):
            prime = check
            pos += 1
        check += 2
    return prime


# Could make it more effecient by using a Prime Sieve (https://en.wikipedia.org/wiki/Generation_of_primes)
print(get_prime_in_position(10001))
