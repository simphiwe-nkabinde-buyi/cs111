# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

from operator import length_hint
import tkinter as tk
from unittest import result
import number_entry as nent
import math


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Heart Rate")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Length:"
    lbl_length = tk.Label(frm_main, text="Length:")

    # Create a integer entry box where the user will enter the length of the pendulum.
    ent_length = nent.IntEntry(frm_main, 0, 100, width=5)

    # Create a label that displays "time:"
    lbl_time = tk.Label(frm_main, text="swinging time:")

    # Create labels that will display the results.
    lbl_result = tk.Label(frm_main, width=4)

    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_length.grid(  row=0, column=0, padx=3, pady=3)
    ent_length.grid(  row=0, column=1, padx=3, pady=3)
    lbl_time.grid(row=0, column=2, padx=(30,3), pady=3)
    lbl_result.grid( row=0, column=3, padx=3, pady=3, columnspan=5)
    btn_clear.grid(row=1, column=0, padx=3, pady=3, columnspan=5, sticky="w")


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the user's age.
            length = ent_length.get()

            # Compute swinging time of pendulum
            result = (2* math.pi) * math.sqrt(length / 9.81)

            # Display the swinging time of pendulum
            lbl_result.config(text=f"{result:.2f}")

        except ValueError:
            # When the user deletes all the digits in the length
            # entry box, clear the result label.
            lbl_result.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_length.delete(0, tk.END)
        lbl_result.config(text="")
        ent_length.focus()


    # Bind the calculate function to the length entry box
    # so that the calculate function will be called when
    # the user changes the text in the entry box.
    ent_length.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the length entry box.
    ent_length.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
