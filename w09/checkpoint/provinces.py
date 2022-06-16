def main():
    #2. Read the contents of the file into a list where each 
    #line of text in the file is stored in a separate element in the list.
    province_list = read_list('./provinces.txt')

    #3. Print the entire list.
    print(province_list)

    #4. Remove the first element from the list.
    province_list.pop(0)
    #5. Remove the last element from the list.
    province_list.pop()

    #6. Replace all occurrences of "AB" in the list with "Alberta".
    replace_list_item(province_list, "AB", "Alberta")

    #7. Count the number of elements that are "Alberta" and print that number.
    count = province_list.count("Alberta")
    print(f"Alberta occurs {count} times in the modified list")



def replace_list_item(list, current, new):
    for i in range(len(list)):
        if list[i] == current:
            list[i] = new

def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    #empty list that stores lines of text from the text file.
    text_list = []

    with open(filename, "rt") as text_file:

        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
        
    return text_list

# Call main to start this program.
if __name__ == "__main__":
    main()