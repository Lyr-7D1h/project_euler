# 5 function calls in 27.000 seconds
def naive(limit):
    m = 10
    s = 13
    for i in range(2, limit):
        x = i
        c = 1
        while x != 1:
            c += 1
            if x % 2 == 0:
                x = x / 2
            else:
                x = x * 3 + 1
        if c > m:
            m = c
            s = i
    return s


# 5226305 function calls in 9.971 seconds
def using_table(limit):
    seq_table = {}
    m = 10
    s = 13
    for i in range(2, limit):
        x = i
        seq = [i]

        while x != 1:
            if x % 2 == 0:
                x = x / 2
            else:
                x = x * 3 + 1
            if x in seq_table:
                seq = seq + seq_table[x]
                break
            seq.append(x)

        seq_table[i] = seq
        if len(seq) > m:
            m = len(seq)
            s = i
    return s


# print(naive(1000000))
print(using_table(1000000))
