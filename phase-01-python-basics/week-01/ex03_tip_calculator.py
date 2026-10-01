# Week 1 — Exercise 3: Tip calculator
# Goal: ask for bill amount and tip %, print total.

# Your code here:

billAmount = int(input("what is your bill"))
tipAmount = int(input("what is your tip percentage?"))
totalAmount = billAmount + (billAmount * tipAmount / 100)
print(f"Your total bill, including tip, is {totalAmount}")
