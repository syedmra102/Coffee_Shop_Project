import sys

resto_name = ("Welcome to The Nexus Coffee").upper()
dashes = "--------------------------------"
order_placement = (f"{1}. Do you want place an order?")
seeing_menu = (f"{2}. Do you want to see the menu?")
exit_option = (f"{3}. Do you want to exit from Nexus coffee?")
selecting_answer = ("For selecting the option using index number like(1,2,3): ")
Starter = (f'                        {dashes}\n                          {resto_name}\n                        {dashes} \n\n {order_placement}\n {seeing_menu}\n {exit_option}')

# Main ordering loop
total_amount = 0
order_items = []

while True:
    print(Starter)
    inp_1 = (int(input(selecting_answer)))

    menu = [

        ("1", "Espresso", 180.0, "Hot Beverages"),
        ("2", "Cappuccino", 220.0, "Hot Beverages"),
        ("3", "Latte", 240.0, "Hot Beverages"),
        ("4", "Mocha", 260.0, "Hot Beverages"),
        ("5", "Cold Coffee", 200.0, "Cold Beverages"),
        ("6", "Iced Americano", 190.0, "Cold Beverages"),
        ("7", "Sandwich", 150.0, "Food"),
        ("8", "Cake Slice", 120.0, "Food"),
        ("9", "Croissant", 100.0, "Food"),
        ("10", "Water Bottle", 50.0, "Others")
    ]

    if inp_1 in [1, 2]:
        print("\nFormatted Menu:")
        print("=" * 50)
        for item in menu:
            print(f"ID: {item[0]:2s} | {item[1]:15} | Rs. {item[2]:6.1f} | Category: {item[3]}")

        # Get order selection with validation
        while True:
            try:
                inp_2 = int(input("\nSelect your order according to serial number (1-10): "))
                if 1 <= inp_2 <= 10:
                    break  # Valid input, exit loop
                else:
                    print(" Invalid! Please enter a number between 1-10")
            except ValueError:
                print(" Invalid! Please enter a number")

    elif inp_1 == 3:
        print("I hope you order next time")
        sys.exit()
    else:
        print(" Invalid syntax")
        continue  # Go back to main menu

    # Now get quantity with validation
    while True:
        try:
            inp_3 = int(input(f"How many {menu[inp_2-1][1]} do you want? "))
            if inp_3 > 10:
                print(" We have only 10 items available!")
            elif inp_3 <= 0:
                print(" Please enter a positive number!")
            else:
                break
        except ValueError:
            print(" Invalid! Please enter a number")

    # Calculate item total and add to order
    item_total = inp_3 * menu[inp_2-1][2]
    total_amount += item_total
    order_items.append(f"{inp_3} x {menu[inp_2-1][1]} - Rs. {item_total}")

    print(f"\n Added to order: {inp_3} x {menu[inp_2-1][1]}")

    # Ask if want anything else
    inp_4 = input("\nDo you want anything else? (Yes/No): ").upper()
    if inp_4 != "YES":
        break

# Final bill
print("\n" + "=" * 50)
print(" FINAL BILL")
print("=" * 50)
for item in order_items:
    print(f"• {item}")
print("=" * 50)
print(f" Total amount: Rs. {total_amount}")
print("=" * 50)
print("Thank you for your order! ")
