"""
Create a python Script to ask user for a number. 
Your program should print countdown of that number to zero.

Example: user enter 5, output should be "5,4,3,2,1,0"
"""

count = int(input("Enter a number: "))
while count >= 0:
   print(count)
   count = count - 1

