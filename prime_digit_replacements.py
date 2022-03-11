def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def has_family(family_size):
    i = 1
    for pos_var in range(2**family_size):
        s = str(i)
        # s[pos_var] = "*"
        c = int(str(i)[pos_var])
        print(c)


# def prime_family(family_size):
#     i = 2
#     while True:
#         if is_prime(i):
#         i += 1

has_family(6)
