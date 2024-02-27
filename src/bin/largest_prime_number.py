def is_prime(x):
    if x > 1:
        for y in range(2, x):
            if x % y == 0:
                return False
    return True


def get_highest_prime(x):
    if is_prime(x):
        return x
    for y in range(2, x):
        devided = x/y
        # Is x devisible by y
        if devided % 1 == 0:
            # Get highest prime of both
            return max(get_highest_prime(int(devided)),
                       get_highest_prime(y))


print(get_highest_prime(600851475143))
