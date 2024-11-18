"""
Create a python Script to ask user for their marks. 
If mark is less than 35, print “You are fail”. 
If mark is greater than or equal to 35, then print “You are pass”.
"""

mark = int(input("enter student mark: "))
if mark < 35:
    print("You are fail")
else:
    print("You are pass")
