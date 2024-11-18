"""
Create a python Script to print first 10 numbers of the fibonacci sequence.
The Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones
Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""

first_no = 0
second_no = 1

count = 10

while count > 0:
    print(first_no)
    sum = first_no + second_no
    first_no = second_no
    second_no = sum

    count = count - 1

