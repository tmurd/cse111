# Import CSV Modual
import csv

# Import DictWriter class from CSV module
from csv import writer

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Define product indexes
PRODUCT_NUMBER_INDEX = 0
PRODUCT_NAME_INDEX = 1
RETAIL_PRICE_INDEX = 2

# Define request indexes
QUANTITY_INDEX = 1

def main():
    try:
        # Read and store file
        # Use to insert into read_dict function
        product_dict = read_dict("products.csv", PRODUCT_NUMBER_INDEX)

        print_product_dict_neat(product_dict)

        print()
        forgot_item = input("Would you like to add any items to your cart (y/n)? ").lower()
        while forgot_item == 'y':
            print()
            product_num = input("What product would you like to add to your request (D150)? ").capitalize()
            num_product = int(input("How much of the product do you need? "))

            add_item_to_request_file(product_num, num_product)
            forgot_item = input("Would you like to add any items to your cart (y/n)? ").lower()

        # Print store name
        print()
        print("Inkom Emporium")

        print()
        #print("Requested Items")

        # Open and read the request.csv file
        with open("request.csv", "rt") as csv_file:

            reader = csv.reader(csv_file)

            # Skip first line of file
            next(reader)

            # Place holders for number of items and subtotal
            num_items = 0
            subtotal = 0

            for row_list in reader:
            # Use the requested product number to find the corresponding item in the products_dict.

                # Establish product_number_index as key to use in product dictionary
                key = row_list[PRODUCT_NUMBER_INDEX]

                # Identify quantity_index as product quantity requested
                quantity = int(row_list[QUANTITY_INDEX])

                # Match key to value in product_dict
                value = product_dict[key]

                # Use value to find product name in product_dict
                product_name = value[PRODUCT_NAME_INDEX]

                # Use value to find retail price in product_dict
                price = float(value[RETAIL_PRICE_INDEX])

                # Print the product name, requested quantity, and product price.
                print(f"{product_name}: {quantity} @ {price}")

                num_items += quantity
                subtotal += price * quantity

        # Calculate sales tax and total
        sales_tax = round(subtotal * 0.06,2)
        total = sales_tax + subtotal

        # Totals listed
        print()
        print(f"Number of Items: {num_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax}")
        print(f"Total: {total:.2f}")

        # Ending receipt information
        print()
        print("Thank you for shopping at Inkom Emporium")
        # Print the current day of the week and the current time.
        print(f"{current_date_and_time:%a %b  %w %X %Y}")
        print()

    # Error message if file isn't found or permissions aren't given
    except (FileNotFoundError, PermissionError) as error:
        print("Error: missing file")
        print(error)

    # Error message if there is an unknown product
    except (KeyError) as error:
        print()
        print(f"Error: unknown product ID in the request.csv file '{key}'")
        print()

# Create dictionary
def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # Create dictionary
    dictionary = {}

    # Read CSV file
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # Skip first line because it is a heading
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # Define product number as key for each row
            key = row_list[key_column_index]

            # Add product number to dictionary as a key
            dictionary[key] = row_list
    
    return dictionary

# Make dictionary neat
def print_product_dict_neat(product_dict):
    print()
    print("Products")
    for product_name, retail_price in product_dict.items():
        print("{} {}".format(product_name, retail_price))


def add_item_to_request_file(product_num, num_product):
    # List of column names 
    list = [product_num, num_product]

    # Open your CSV file in append mode
    # Create a file object for this file
    with open('request.csv', 'a', newline='') as csv_file:

        # Pass the csv_file and a list 
        # of the products
        writer_object = writer(csv_file)

        #Pass the list as an argument to the Writerow()
        writer_object.writerow(list)

        #Close the csv file
        csv_file.close()
  

# Call main to start this program.
if __name__ == "__main__":
    main()