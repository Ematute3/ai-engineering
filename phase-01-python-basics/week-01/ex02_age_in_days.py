# Week 1 — Exercise 2: Age in days
# Goal: ask the user for their age, print how many days old they are.
# Assume 365 days/year (ignore leap years).

# Your code here:
name = input("What is your name?")
age = int(input("how old are you?"))
dayOld = age * 365
print(f"{name} your {dayOld} days old")
