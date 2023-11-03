x =lambda a, b: a ** b
print(x(2, 10))

numbers = [1,2,5,9,15]

def filter_numbers(num):
    nums = [1, 5, 17]
    if num in nums:
        return True
    else:
        return False


filtered_numbers = filter(filter_numbers, numbers)
for n in filtered_numbers:
    print(n)

def o(p):
    def q():
        return '*' * p
    return q

r = o(1)
s = o(2)
print(r() + s())

print('------------------------')

def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s
    
for x in fun(2):
    print(x, end = '')