def d(n):
    sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum += i

    return sum


sum = 0
for i in range(1, 10000):
    a = d(i)
    if a != i and d(a) == i:
        sum += i

# 19998 function calls in 2.276 seconds
print(sum)
