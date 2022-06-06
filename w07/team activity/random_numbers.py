
import random
from traceback import print_tb

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")

    append_random_numbers(numbers)
    print(f"numbers {numbers}")

    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")


def append_random_numbers(numbers_list, quantity=1):
    """Append quantity random numbers onto the numbers list.
    The random numbers are between 0 and 100, inclusive.
    Parameters
        numbers_list: A list of numbers where this function will
            append random numbers.
        quantity: The number of random numbers that this function
            will append onto numbers_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the numbers_list.
    """
    
    for _ in range(quantity):
        random_num = random.uniform(1, 100)
        rounded = round(random_num, 1)
        numbers_list.append(rounded)




# Call main to start this program.
if __name__ == "__main__":
    main()