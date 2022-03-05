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
start_day = 0  # Start on monday

for year in range(1900, 2001):
    if year % 4 == 0 and not (year % 100 == 0 and year % 400):
        months[1] = 29

    for month, days in enumerate(months):
        if month == 0:
            sundays += (start_day + days) // 7
            print(
                f"{year} {month} starting on {start_day} has ", (start_day + days) // 7
            )
        start_day = days % 7


print(sundays)
