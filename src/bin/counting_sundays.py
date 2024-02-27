months = [
    31,  # jan
    28,  # feb
    31,  # mar
    30,  # apr
    31,  # may
    30,  # jun
    31,  # jul
    31,  # aug
    30,  # sep
    31,  # okt
    30,  # nov
    31,  # dec
]

sundays = 0
start_day = 1  # Start on monday

for year in range(1901, 2001):
    months[1] = 28
    if year % 4 == 0 and not (year % 100 == 0 and year % 400):
        months[1] = 29

    for month, days in enumerate(months):
        if start_day == 6:
            sundays += 1
        start_day = (days + start_day) % 7


print(sundays)
