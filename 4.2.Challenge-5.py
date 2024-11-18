"""
Create a python Script to ask user for a number. 
If number is divisible by 2, print “ your number is EVEN”. 
If number is not divisible by 2, then print “your number is ODD”.
"""
my_no = int(input("enter a number: "))
if my_no % 2 == 0:
    print("EVEN")
else:
    print("ODD")