

def naive(divisble_limit):
    divisible_count = 0
    x = 1
    while divisible_count < divisble_limit:
        divisible_count = 0
        x += 1
        t = int(x * (x + 1) / 2)

        for i in range(1, int(t ** 0.5) + 1):
            if t % i == 0:
                # divisible_count += 1
                # If divisors are equal,
                # count only one
                if (t / i == i):
                    divisible_count += 1
                else:  # Otherwise count both
                    divisible_count += 2
        print(t, divisible_count)
    return t


print(naive(5))
