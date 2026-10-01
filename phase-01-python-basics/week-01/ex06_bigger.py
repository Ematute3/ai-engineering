# Week 1 — Exercise 6: Bigger of two
# Goal: ask for two numbers, print the bigger one. Print "they're equal" if so.

# Your code here:

num1 = float(input(" first number"))
num2 = float(input("second number"))
if num1 > num2:
    print("the bigger number is", num1)
else:
    if num2 > num1:
        print("the bigger number is", num2)
    else:
        print("they're equal")