def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)


sum = 0
for c in str(factorial(100)):
    sum += int(c)

print(sum)
