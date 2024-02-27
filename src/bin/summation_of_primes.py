# 2000005 function calls in 2.141 seconds
def my_shitty_sieve_of_sundaram(limit):
    f = [True] * limit

    for i in range(1, limit):
        for j in range(i, limit):
            comp_index = i + j + (2 * i * j)
            if (comp_index > limit):
                break
            f[comp_index - 1] = False

    sum = 2
    for i in range(1, limit // 2):
        if i > limit:
            break
        if f[i - 1]:
            sum += i * 2 + 1

    return sum


print(my_shitty_sieve_of_sundaram(2000000))
