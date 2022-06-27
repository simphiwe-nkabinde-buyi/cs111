from datetime import datetime
import csv

def main():
    try:
        product_dict = read_dict('products.csv', 0)
        request_list = read_list('request.csv')

        print_receipt(product_dict, request_list)

    except KeyError as key_err:
        print()
        print(type(key_err).__name__,f"{key_err} is not an existing product ", sep=':' )

    except ( FileNotFoundError, PermissionError ) as error:
        print()
        print(error)     
        print("Please choose a different file.")   




def print_receipt(product_dict, request_list):
    """Print name, price and qty of each requested item.
    print number of items, subtotal, sales tax and total
    price of requested items.
    
    Parameters:
        product_dict: a compound dictionary of the products. { product_id: [product_id, name, price] }
        request_list: a compound list of each request [ product, quantity ].
    """

    print('\nInkom Emporium\n')
    total_items = 0
    subtotal_price = 0

    PRODUCT_NUM_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
    RECEIPT_QTY_INDEX = 1

    for row_list in request_list:
        product_num = row_list[PRODUCT_NUM_INDEX]
        product = product_dict[product_num]
        name = product[PRODUCT_NAME_INDEX]
        qty = row_list[RECEIPT_QTY_INDEX]
        price = product[PRODUCT_PRICE_INDEX]
        print(f"{name}: {qty} @ {price}")

        total_items += int(qty)
        subtotal_price += (int(qty) * float(price))

    sales_tax = subtotal_price * 0.06
    total_price = subtotal_price + sales_tax
    current_date_and_time = datetime.now()

    #discount the product prices by 10% if today is Tuesday or Wednesday.
    discount_amount = 0
    discounted_total = 0
    if (current_date_and_time.weekday() == 1) or (current_date_and_time.weekday() == 2):
        discount_amount = total_price * 0.1
        discounted_total = total_price - discount_amount

    print()
    print(f"Number of Items: {total_items}")
    print(f"Subtotal: {subtotal_price:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total_price:.2f}")
    
    if discount_amount != 0: 
        print(f"\n!!Tuesday/Wednesday discount: 10% off all products!! ")
        print(f"New Total: {discounted_total:.2f}")
        print(f"You saved {discount_amount:.2f}")

    print("\nThank you for shopping at the Inkom Emporium.")
    print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")


def read_list(filename):
    """Read the contents of a CSV file into a
    compound list and return the list

    parameters
        filename: the name of the CSV file to read.
    Return: a compound list that contains the 
        contents of the CSV file.
    """
    compound_list = []
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for list in reader:
            compound_list.append(list)
        
        return compound_list

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
