# Week 1 — Exercise 10: Receipt
# Goal: ask for 3 items with prices; print a formatted receipt.
# Example output:
#   Item 1: $4.50
#   Item 2: $12.00
#   Item 3: $0.99
#   Total:  $17.49

item1 = input("enter item 1")
price1 = float(input("enter price for item 1"))
item2 = input("enter item 2")
price2 = float(input("enter price for item 2"))
item3 = input("enter item 3")
price3 = float(input("enter price for item 3"))
total = price1 + price2 + price3
print(f"Item 1: ${price1:.2f}")
print(f"Item 2: ${price2:.2f}")
print(f"Item 3: ${price3:.2f}")
print(f"Total:  ${total:.2f}")
