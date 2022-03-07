# Obtain math library
import math
# Obtain os library for openning file
import os
# Insert datetime library
from datetime import datetime

# Calculate current date
current_date_and_time = datetime.now()
# Calculate current hour
current_time = current_date_and_time.time().hour

# Set value for 'while' loop
repeat = None

# Based on the time of day, the code will give the customer a differnet greeting
print()
if current_time < 12:
    customer_name = input("Good morning valued customer! Please enter your first and last name (ex Sean Smith): ")
elif current_time >= 12 and current_time < 17:
    customer_name = input("Good afternoon valued customer! Please enter your first and last name (ex Sean Smith): ")
else:
    customer_name = input("Good evening valued customer! Please enter your first and last name (ex Sean Smith): ")

while repeat != "n":
    # Obtain tire information form user
    print()
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    # Calculate approximate volume
    volume = ((math.pi*(width*width)*ratio)*(width*ratio+2540*diameter))/(10000000000)

    # Display approximate volume
    print()
    print(f"The approximate volume of the tire is {volume :.2f} liters")
    print()

    # Attach user inputs to text file
    with open("volumes.txt", mode='at') as vol_file:
        print(f"{customer_name}, {current_date_and_time:%Y-%m-%d}, W={width}, AR={ratio}, D={diameter}, V={volume :.2f}", file=vol_file)

    # Ask customer if they need to enter another tire size
    repeat = input("Do you need to enter another tire size (y/n)? ")

# Open text file
print()
show = input("Would you like to open the text file to see the information (y/n)? ")
print()
if show == "y" or show == "Y":
    os.startfile('C:\\Users\\briti\\OneDrive - BYU-Idaho\\Documents\\CSE111\\volumes.txt')
else:
    print("Oaky. Nothing was opened.")