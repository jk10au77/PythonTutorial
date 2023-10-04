"""
    Lists in advanced application:
    ------------------------------
    Elements of a list can be 
        a. Scalar i.e. numbers and much more complex struture like strings, booleans, even another list         
"""

"""
        List comprehensions:
        ----------------------
        a. is a special syntax used to fill large list
        b. List comprehesion is actually a list.
        c. We can creat a list using list comprehesnion on-the-fly 

"""
# List comprehension examples:

squares = [x ** 2 for x in range(1, 26)]
print(squares)
odds = [x for x in squares if x % 2 != 0]   # produces odd numbers 
print(odds)

"""
    Lists in list - 2-Dimensional arrays
    This concept can be understood by using the chess design layout. 
    Let 'EMPTY' be an empty field on the chessboard
"""

# Create a list of lists representing the whole chessboard 

board = []
EMPTY = 0
for i in range(8):
    row = [EMPTY for i in range(8)] # creates a row consisting of eight elements.
    board.append(row)           # the row is appended to the board. In total board consist of 64 elements

for line in board:
    print(line)

# The board can also created by using list comprehension as shown below

print("Board creation using list comprehensions.")
board = [[EMPTY for i in range(8)] for j in range(8)]   #the inner part creates a row and outter part builds a list of rows
for i in board:
    print(i)
 

   
