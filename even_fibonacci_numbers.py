sum = 2
x = 1
y = 2
while sum < 4 * 10 ** 6:
    localSum = x + y
    x = y
    y = localSum
    if localSum % 2 == 0:
        sum += localSum

print(sum)
