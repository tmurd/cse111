def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print()
    print(f"original: {fruit_list}")

    # Reverse list order
    fruit_list.reverse()
    print()
    print(f"reversed: {fruit_list}")

    # Add orange to the list
    fruit_list.append("orange")
    print()
    print(f"append orange: {fruit_list}")
    
    # Find apple in the list and add cherry before apple
    index = fruit_list.index("apple")
    fruit_list.insert(index, "cherry")
    print()
    print(f"insert cherry: {fruit_list}")

    # Remove banana from list
    fruit_list.remove("banana")
    print()
    print(f"remove banana: {fruit_list}")

    # Remove last element from list
    last = fruit_list.pop()
    print()
    print(f"pop {last}: {fruit_list}")

    # Sort and print fruit_list
    fruit_list.sort()
    print()
    print(f"sorted: {fruit_list}")

    # Clear and print the fruit_list
    fruit_list.clear()
    print()
    print(f"cleared: {fruit_list}")
    print()

if __name__ == "__main__":
    main()
