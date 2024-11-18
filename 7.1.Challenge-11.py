# Write a function to add two numbers, which takes two paraments and returns the sum.

def add(no1, no2):
    total = no1 + no2
    return total

number1 = int(input("Enter First number: "))
number2 = int(input("Enter Second number: "))
sum = add (number1, number2)
print("Sum = ", sum)