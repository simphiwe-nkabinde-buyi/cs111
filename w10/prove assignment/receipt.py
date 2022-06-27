import csv

def main():
    # Calls the read_dict function and stores the compound dictionary in a variable named products_dict.
    product_dict = read_dict('products.csv', 0)

    # Prints the products_dict.
    print(product_dict)
    
    #Print each product name, requested quantity, and product price of receipt.
    print('\nRequested Items')
    with open('request.csv', "rt") as request_csv:
        reader = csv.reader(request_csv)
        next(reader)

        PRODUCT_NUM_INDEX = 0
        PRODUCT_NAME_INDEX = 1
        PRODUCT_PRICE_INDEX = 2
        RECEIPT_QTY_INDEX = 1

        for row_list in reader:
            product_num = row_list[PRODUCT_NUM_INDEX]
            product = product_dict.get(product_num)
            name = product[PRODUCT_NAME_INDEX]
            qty = row_list[RECEIPT_QTY_INDEX]
            price = product[PRODUCT_PRICE_INDEX]
            print(f"{name}: {qty} @ {price}")


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

            key = row_list[key_column_index]
            dictionary[key] = row_list

    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()
