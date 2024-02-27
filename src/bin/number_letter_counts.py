dic = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}


def get_string(num):
    string = str(num)
    # 100 - 9999
    if len(string) > 2:
        res = ""
        for pos, char in enumerate(string):
            pos = len(string) - pos - 1
            if char == "0":
                continue
            if pos < 2:
                res += "and" + get_string(int(string[-pos-1:]))
                break
            if pos >= 2:
                res += dic[int(string[0])] + dic[10 ** (pos)]
        return res

    # 1-100
    if num in dic:
        return dic[num]

    if len(string) == 2:
        return dic[int(string[0]) * 10] + dic[int(string[1])]


def count_written_numbers(limit):
    sum = 0
    for num in range(1, limit + 1):
        res = get_string(num)
        sum += len(res)
    return sum


# 7401 function calls (6510 primitive calls) in 0.003 seconds
print(count_written_numbers(1000))
