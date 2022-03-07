import random

def main():

    # Beginning number list
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")
    
    # Add one random number to list
    append_random_numbers(numbers)
    print(f"numbers {numbers}")

    # Add 3 more random numbers to list
    append_random_numbers(numbers, quantity=3)
    print(f"numbers {numbers}")

    # Create word list
    words = []
    
    # Add radom words to word list
    append_random_words(words, quantity=6)
    print(f"words   {words}")

# Add random number to the numbers list
def append_random_numbers(number_list, quantity=1):

    # Loops through appending random numbers for given quantity perameter
    for _ in range(quantity):
        # Choose random number from 1-100
        random_num = random.uniform(0, 101)
        
        # Round random number to 1 decimal place
        round_num = round(random_num, 1)
        
        # Add random number to the end of the number list
        number_list.append(round_num)

def append_random_words(words_list, quantity=1):

    for _ in range(quantity):
        words = ("weird", "funny", "blue", "humorous", "jolly", "cute", "pretty", "ugly", "smart", "intresting", "awkward", "playful", "dirty")
        random_word = random.choice(words)
        words_list.append(random_word)

# If main is not imported, call the main function
if __name__ == "__main__":
    print()
    main()
    print()