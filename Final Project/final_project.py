# Import JSON Modual
import json

# Import Pretty Print Modual
import pprint

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

inventory = {}
checked_out_items = {}

def main():
    with open("inventory.json") as inventory_file:
        inventory = json.load(inventory_file)

    print()
    print("1. Check Out Item\n2. Check In Item\n3. Exit")
    print()
    action = int(input("What would you like to do? "))
    if action == 1:
        print()
        display_inventory()
        print()
        check_out_items(inventory)
    elif action == 2:
        print()
        display_inventory()
        print()
        check_in_items(inventory)
    elif action == 3:
        pass
    

def display_inventory():
    # Open and read checked_out.json file
    with open("inventory.json", "r") as outfile:
        item_list = json.load(outfile)
    
    # Print the item list in a good looking format
    print("ITEM LIST")
    pprint.pprint(item_list)

def check_out_items(inventory):
    """
    Collect all the infomation needed from the user to check out
    items from the material library. Collect: name, item, and quantity.
    Call the create_checked_out_dict function to save user inputs in 
    checked_out.json file. Make sure user can checkout multiple 
    different items to a single person.
    """
    # Set more_items variable
    more_items = "y"

    # Allow user to add more items
    while more_items != "n":

        # Have user type their name and append to list
        name = input("what is your first and last name (John Smith)? ")

        # Have user type the item they want to check out
        # and how many they want to check out
        item_num = input("What item would you like to check out (A001)? ")
        quantity = int(input("How many do you need? "))

        # Call function that creates and writes to checked_out.json file
        add_to_checked_out_dict(name, item_num, quantity)

        # Call function that removes item from inventory.json
        remove_from_inventory(item_num, quantity)

        # Ask user if they need to check out more items
        more_items = input("Do you need to check out another item (y/n)? ").lower()

def remove_from_inventory(item_num, quantity):
    # Open and read checked_out.json file
    with open("inventory.json", "r") as outfile:
        inventory_out = json.load(outfile)

    # Find the item name in checked out json file
    if item_num in inventory_out:
        inventory_out[item_num]["quantity"] = inventory_out[item_num]["quantity"] - quantity

    # Write variable user inputs to checked_out.json
    with open("inventory.json", "w") as outfile:
        outfile.write(json.dumps(inventory_out, indent = 4))
        

def add_to_checked_out_dict(name, item_num, quantity):
    """
    Open the checked_out.json file to read. Pass in name of person, 
    item_out, and quantity into the Checked Out dictionary in the 
    checked_out.json file. Use the name of the person as the 
    disctionary title. Write user inputs to checked_out.json file.
    """
    # Open and read checked_out.json file
    with open("checked_out.json", "r") as outfile:
        item_out = json.load(outfile)
    
    # Create a time_stamp variable
    time_stamp = f"{current_date_and_time:%Y-%m-%d %H:%M}"

    # Pull user inputs to be insterted into checked_out.json
    item_info = {
        "item_num": item_num,
        "quantity": quantity,
        "time_stamp": time_stamp
        }

    if name in item_out["Checked Out"]:
        item_out["Checked Out"][name].append(item_info)
    else:
        item_out["Checked Out"][name] = [item_info]

    # Place item_info in Checked Out dictionary with the name of
    # the person as the title to create multiple objects

    # Write variable user inputs to checked_out.json
    with open("checked_out.json", "w") as outfile:
        outfile.write(json.dumps(item_out, indent = 4))

def check_in_items(inventory):
    # Set more_items variable
    more_items = "y"

    # Allow user to add more items
    while more_items != "n":

        # Have user type their name and append to list
        name = input("what is your first and last name (John Smith)? ")

        # Have user type the item they want to check in
        # and how many they want to check in
        item_num = input("What item would you like to check in (A001)? ")
        quantity = int(input("How many are you checking in? "))
        inventory[item_num]["quantity"] = inventory[item_num]["quantity"] + quantity
        item_in = inventory[item_num]
        
        # Call function to remove item from checked_out.json
        remove_item_from_check_out(name, item_num, quantity)

        # Call function to add item quantity to inventory.json
        add_quantity_to_inventory(item_num, quantity)

        # Ask user if they need to check in more items
        more_items = input("Do you need to check in another item (y/n)? ").lower()

def remove_item_from_check_out(name, item_num, quantity):
    # Open and read checked_out.json file
    with open("checked_out.json", "r") as outfile:
        item_in = json.load(outfile)
    
    # Find the name in checked out json file
    if name in item_in["Checked Out"]:

        # Loop through the name until the correct item is found
        for i in item_in["Checked Out"][name]:
            if i["item_num"] == item_num:

                # Remove item in list if the quantity is equal to 
                # or greater than the checked out quantity
                if quantity >= i["quantity"]:
                    item_in["Checked Out"][name].remove(i)
                
                # Do not remove the item, but subtract the quantity
                # of the item if quantity is less than checked out quantity
                else:
                    i["quantity"] -= quantity

        #del item_in["Checked Out"][name]

    # Write variable user inputs to checked_out.json
    with open("checked_out.json", "w") as outfile:
        outfile.write(json.dumps(item_in, indent = 4))

def add_quantity_to_inventory(item_num, quantity):
    # Open and read checked_out.json file
    with open("inventory.json", "r") as outfile:
        inventory_in = json.load(outfile)

    # Find the item name in checked out json file
    if item_num in inventory_in:
        inventory_in[item_num]["quantity"] = inventory_in[item_num]["quantity"] + quantity

    # Write variable user inputs to checked_out.json
    with open("inventory.json", "w") as outfile:
        outfile.write(json.dumps(inventory_in, indent = 4))

# Call the main function
if __name__ == "__main__":
    main()