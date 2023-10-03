"""
    1. This python snippet generates numeric basic arithematic expressions 
    2. The expressions, thus, generated are used to conduct daily exams for class 3 to class 5 students.

"""
import random
operations = ['+', '-']



def evaluate(number_1, number_2, operate):
    if operate == '+':
        value = number_1.__add__(number_2)
        return value
    else:
        if number_1 > number_2:
            value = number_1.__sub__(number_2)
            return value
        else:
            number_1, number_2 = number_2, number_1
            value = number_1.__sub__(number_2)
            return value

max = 100      

for count in range(1, 101):
    number_1 = random.randint(100, 1000)
    number_2 = random.randint(100, 1000)
    operate = random.choice(operations)
    
    value = evaluate(number_1, number_2, operate)
    expr = f'{count}) {number_1} {operate} {number_2} = {value}'
    print(expr)


