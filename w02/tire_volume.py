import math
from datetime import datetime

PI = math.pi

w = float(input("Enter the width of the tire in mm (ex 205):"))
a = float(input("Enter the aspect ratio of the tire (ex 60):"))
d = float(input("Enter the diameter of the wheel in inches (ex 15):"))

volume = (PI * w**2 * a * (w * a + 2540 * d)) / 10000000000

print(f"The approximate volume is: {volume:.2f} liters")

current_date = datetime.now()

# Open a text file named cities.txt in append mode.
with open("volumes.txt", "at") as volumes_file:

    print(f"{current_date:%Y-%m-%d}, {w}, {a}, {d}, {volume:.2f}", file=volumes_file)

