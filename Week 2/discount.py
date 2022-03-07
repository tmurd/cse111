"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store's slowest sales days. 
On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, the store will discount the customer's subtotal by 10%.
"""

# Insert datetime library
from datetime import datetime

# Calculate current date into number
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

# Starting values for loops
user_subtotal = 0
price = 1
answer = None

# Directions for user
print()
print(f"Enter a 0 for the price if you have no more items")
print()

# Initail loop for customer purchases
while price != 0:
    price = float(input("Enter the price: $"))
    if price != 0:
        quantity = int(input("Enter the quantity: "))
        user_subtotal += price*quantity
        print()

# Large loop to help customer achieve discount
while answer != "y":
   
    # Ask user if they'd like a discount
    if user_subtotal < 50 and (day_of_week == 1 or day_of_week == 2):
        diff = 50 - user_subtotal
        print()
        print(f"Spend ${diff :.2f} more and receive a 10% discount!")

    # Customer receivces the discount
    elif user_subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
        print()
        print(f"Hurray! You got the 10% discount!")

    # Ask the customer if they'd like to continue to checkout
    print()
    answer = input("Would you like to continue to check out (y/n)? ")
    print()

    # Have customer input additionally purchased items through another loop
    if answer == "n":
        price = 1
        print(f"Enter a 0 for the price if you have no more items")
        print()
        while price != 0:
            price = float(input("Enter the price: $"))
            if price != 0:
                quantity = int(input("Enter the quantity: "))
                user_subtotal += price*quantity
                print()
    
# Calculate subtotals if discount applies for Tuesday or Wednesday
print()
if user_subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = user_subtotal * 0.10
    discount_subtotal = user_subtotal - discount
    tax = discount_subtotal * 0.06
    amount_due = tax + discount_subtotal
    print(f"Discount amount: ${discount :.2f}")
    print(f"Sales tax amount: ${tax :.2f}")
    print(f"Total: ${amount_due :.2f}")
    print()

# Calculate subtotals if NOT Tuesday or Wednesday
else:
    tax = user_subtotal * 0.06
    amount_due = tax + user_subtotal
    print(f"Sales tax amount: ${tax :.2f}")
    print(f"Total: ${amount_due :.2f}")
    print()