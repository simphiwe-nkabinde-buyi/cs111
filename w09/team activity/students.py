import csv

def main():

    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    students_dict = read_dict('students.csv', I_NUMBER_INDEX)

    i_number = input("Please enter an I-Number (xxxxxxxxx): ")
    i_number = i_number.replace('-', '')

    if not i_number.isdigit():
        print("Invalid I-Number")
    elif len(i_number) < 9:
        print("Invalid I-Number: too few digits" )
    elif len(i_number) > 9:
        print("Invalid I-Number: too many digits")

    else:
        student_name = students_dict.get(i_number)
        if student_name == None:
            print("No such student")
        else:
            print(student_name[NAME_INDEX])





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
    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:

            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()