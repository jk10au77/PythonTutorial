"""
    This is the firts program you learn in the world of computer programming.
    This prints the 'Hello, World' message.
"""

print("Hello, World!")  # prints the message in the double quotes.

name = 'Jaya Kumar'
hello = 'Hello,'   
print(hello, name)

def printcalendar(year):
    for yr in year:
        for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December']:
                print(f'\t {month} {yr}')
                print("Mo  ","Tu  ","We  ","Th  ","Fr  ","Sa  ","Su")
                print('\n\n')
            
printcalendar([2020, 2021, 2022, 2023])