
def main():
    # Read and store file
    provinces_list = read_file("provinces.txt")

    # Print entire list
    print()
    print(provinces_list)

    # Remove first element in list
    provinces_list.pop(0)

    # Remove last element in list
    provinces_list.pop()

    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
    
    count = provinces_list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list.")
    print()

def read_file(filename):
    
    text_list = []

    with open(filename, "rt") as text_file:
        
        for line in text_file:
            strip_line = line.strip()
            text_list.append(strip_line)
    
    return text_list

if __name__ == "__main__":
    main()