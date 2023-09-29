"""
History of changes:
--------------------
S.No  Version Number  Description
---------------------------------------------
1.     1.01           Lothar Collatz hypothesis states that regardless of initial value of c0, it always goes to 1 when
                        anyone performs the below steps: 
                            a. take any non-negative and non-zero integer say c0
                            b. if it's even evaluate a new c0 as c0 / 2;
                            c. otherwise, if it's odd evaluate a new c0 as 3 * c0 + 1;
                            d. if c0 != 1, go to step b
2.     1.02             The above is implemented using functions. Here the input integer is stored in list.Then
                        for each number in the list is tested for Lothar Collatz ypothesis.
                        define the collatz() which takes a non-zero and non-negative integer

"""
number = int(input("Enter any non-zero non-negative integer: "))
count = 0
print_message = "The number of steps required to achieve goal are: "
while number != 1:
    remainder = number % 2
    if remainder == 0:
        number = number // 2
        count += 1
        print(number) 
    else:
        number = number * 3 + 1
        count += 1
        print(number)
print(print_message, count)

"""
    Implemeting version 1.01 using functions

"""
numbers = [10,20,50, 1265]
count = 0

def print_msg(number):
    print(number)

def print_count(print_message, count):
    print(print_message, count) 

def collatz(number):
    count = 0
    while number != 1:
        if remainder == number % 2:
            number = number // 2
            count += 1
            print_msg(number)
        else:
            number = 3 * number + 1
            count += 1
            print_msg(number)
    print_count(print_message, count)


for num in numbers:
    print("The inital number is ", num)
    collatz(num)
    print("------------------------------------------")
print("End of Lothat Collatz hypothesis.")

