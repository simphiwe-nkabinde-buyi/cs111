from datetime import datetime

current_datetime = datetime.now()
weekday = current_datetime.weekday()

subtotal = float(input("Please enter the subtotal: "))
sales_tax = (6/100) * subtotal
discount_amount = 0.1 * subtotal
balance_amount = subtotal + sales_tax - discount_amount

if subtotal >= 50 and (weekday == 1 or weekday == 2):
    print(f"discount amount: {discount_amount:.2f}")
    print(f"Sales tax amount: {sales_tax:.2f}")
    print(f"Total: {balance_amount:.2f}")
# else:
#     total = sales_tax + subtotal
#     print(f"Sales tax amount: {sales_tax}")
#     print(f"Total: {total}")