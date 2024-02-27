def sum_squares(x):
    sum = 0
    for i in range(1, x + 1):
        sum += i ** 2
    return sum


def square_sum(x):
    sum = 0
    for i in range(1, x + 1):
        sum += i
    return sum ** 2


print(square_sum(100) - sum_squares(100))
