# 0.408
def brute():
    a = b = max = 0
    for x in range(1000):
        for y in range(1000):
            res = x * y
            if str(res) == str(res)[::-1]:
                if res > max:
                    max = res
                    a = x
                    b = y

    return max


# 0.008
def efficient_brute():
    m = 0
    for x in range(999, 0, -1):
        # https://www.google.com/search?channel=fs&client=ubuntu&q=palindrome+numbers+divisible
        for y in range(990, 0, -11):
            res = x * y
            if res > m:
                if str(res) == str(res)[::-1]:
                    m = res
                    break
    return m


print(efficient_brute())
