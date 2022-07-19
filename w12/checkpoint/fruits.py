def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")

        # reverse and print fruit_list.
        fruit_list.reverse()
        print(f"reversed: {fruit_list}")

        # append "orange" to the end of fruit_list and print the list.
        fruit_list.append("orange")
        print(f"append orange: {fruit_list}")

        # find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
        index = fruit_list.index("apple")
        fruit_list.insert(index, "cherry")
        print(f"insert cherry: {fruit_list}")

        # remove "banana" from fruit_list and print the list.
        fruit_list.remove("banana")
        print(f"remove banana: {fruit_list}")

        #pop the last element from fruit_list and print the popped element and the list.
        popped = fruit_list.pop()
        print(f"pop {popped}: {fruit_list}")

        # sort and print fruit_list.
        fruit_list.sort()
        print(f"sorted: {fruit_list}")

        # clear and print fruit_list.
        fruit_list.clear()
        print(f"cleared: {fruit_list}")
    
    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")


# Call main to start this program.
if __name__ == "__main__":
    main()