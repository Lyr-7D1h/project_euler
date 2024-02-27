# 30975 function calls in 0.009 seconds

total = 0
with open("data/names.txt") as f:
    names = f.read().replace('"', "").split(",")
    names.sort()
    for i, name in enumerate(names):
        val = 0
        for c in name:
            val += ord(c) - 64
        total += val * (i + 1)

print(total)
