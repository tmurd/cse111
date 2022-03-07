# Import CSV modual
import csv

def main():
    # Define Indexes
    I_NUMBER_INDEX = 0
    STUDENT_NAME_INDEX = 1

    # Read and store file
    # Use to insert into read_dict function
    student_dict = read_dict("students.csv", I_NUMBER_INDEX)

    # Have user enter INumber
    print()
    inumber = input("Please enter a student I-Number (xxxxxxxxx): ")

    # If user adds dashes, remove them
    inumber = inumber.replace("-", "")

    # Determine if user input is a number and has 9 digits
    if not inumber.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(inumber) < 9:
            print("Invalid I-Number: too few digits")
        elif len(inumber) > 9:
            print("Invalid I-Number: too many digits")
        else:
            # The user input is a valid I-Number
            # Check if the I-Number is a key that is in the dictionary.
            if inumber in student_dict: 
            
                # Find line containing INumber
                value = student_dict[inumber]

                # Find student name with specified INumber
                student_name = value[STUDENT_NAME_INDEX]

                # Print student name
                print()
                print(student_name)
                print()

            else:
                # Print a message saying no such student
                print("No such student")
                print()

# Read file and create a dictionary
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

            # Define Inumber as key for each row
            key = row_list[key_column_index]

            # Add INumber to dictionary as a key
            dictionary[key] = row_list
    
    # Create filled dictionary
    return dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()