import calendar             # import calendar module

class_dir = [name for name in dir(calendar)]

#print(class_dir, end='\n')
"""
for i in range(7):
    if i == 0:
        print(calendar.MONDAY)
    elif i == 1:
        print(calendar.TUESDAY)
    elif i == 2:
        print(calendar.WEDNESDAY)
    elif i == 3:
        print(calendar.THURSDAY)
    elif i == 4:
        print(calendar.FRIDAY)
    elif i == 5:
        print(calendar.SATURDAY)
    elif i == 6:
        print(calendar.SUNDAY)
        """
"""
for cal in range(2020, 2025):
    print(calendar.calendar(cal))

for cal in range(2020, 2025):
    calendar.prcal(cal)
    """
"""
for year in range(2020, 2025):
    for mon in range(1, 13):
        print(calendar.month(year, mon))
    """

for year in range(2020, 2025):
    for mon in range(1,13):
        calendar.prmonth(year, mon)

