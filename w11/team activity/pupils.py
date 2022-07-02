import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():

    students_list = read_compound_list('pupils.csv')

    birthdate_func = lambda student: student[BIRTHDATE_INDEX]
    name_func = lambda student: student[GIVEN_NAME_INDEX] + student[SURNAME_INDEX]
    birthmonthday_func = lambda student: student[BIRTHDATE_INDEX][4:]
    
    sorted_by_birthdate = sorted(students_list, key=birthdate_func)
    sorted_by_name = sorted(students_list, key=name_func)
    sorted_by_birthmonthday = sorted(students_list, key=birthmonthday_func)

    print('Ordered from Oldest to Youngest')
    print_list(sorted_by_birthdate)

    print('\nOrdered by Given Name')
    print_list(sorted_by_name)

    print('\nOrdered by Birth Month and Day')
    print_list(sorted_by_birthmonthday)

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(compound_list):
    """Print the elements in a compound list to
    the terminal window for the user to see.

    Parameter
        compound_list: a list that contains other lists
    Return: nothing
    """

    for item in compound_list:
        print(item)


# If this file is executed like this:
# > python add_area_code.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
