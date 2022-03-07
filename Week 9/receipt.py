# Import CSV Modual
import csv

# Define product indexes
PRODUCT_NUMBER_INDEX = 0
PRODUCT_NAME_INDEX = 1
RETAIL_PRICE_INDEX = 2

# Define request indexes
QUANTITY_INDEX = 1

def main():

    # Read and store file
    # Use to insert into read_dict function
    product_dict = read_dict("products.csv", PRODUCT_NUMBER_INDEX)

    print_product_dict_neat(product_dict)

    print()
    print("Requested Items")
    with open("request.csv", "rt") as csv_file:
        
        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:
        # Use the requested product number to find the corresponding item in the products_dict.

            # Establish product_number_index as key to use in product dictionary
            key = row_list[PRODUCT_NUMBER_INDEX]

            # Identify quantity_index as product quantity requested
            quantity = row_list[QUANTITY_INDEX]

            # Match key to value in product_dict
            value = product_dict[key]

            # Use value to find product name in product_dict
            product_name = value[PRODUCT_NAME_INDEX]

            # Use value to find retail price in product_dict
            price = value[RETAIL_PRICE_INDEX]

        
            # Print the product name, requested quantity, and product price.
            print(f"{product_name}: {quantity} @ {price}")
    
    print()


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

def print_product_dict_neat(product_dict):
    print()
    print("Products")
    for product_name, retail_price in product_dict.items():
        print("{} {}".format(product_name, retail_price))

# Call main to start this program.
if __name__ == "__main__":
    main()