# Since the restaurant name is unlikely to change, this can be a global constant
RESTAURANT_NAME = "Blue Bird"
# Using a nested dictionary for the menu

menu = {
    "sku1" : {
        "name": "Hamburger",
        "price": 6.51
    },
    "sku2" : {
        "name": "Cheeseburger",
        "price": 7.75
    },
    "sku3": {
        "name": "Milkshake",
        "price": 5.99
    },
    "sku4": {
        "name": "Fries",
        "price": 2.39
    },
    "sku5": {
        "name": "Sub",
        "price": 5.87
    },
    "sku6": {
        "name": "Ice Cream",
        "price": 1.55
    }, 
    "sku7": {
        "name": "Fountain Drink",
        "price": 3.45
    },
    "sku8": {
        "name": "Cookie",
        "price": 3.15
    },
    "sku9": {
        "name": "Brownie",
        "price": 2.46
    },
    "sku10": {
        "name": "Sauce",
        "price": 0.75
        }
}


app_actions = {
    "1": "Add a new menu item to cart",
    "2": "Remove an item from the cart",
    "3": "Modify a cart item's quantity",
    "4": "View cart",
    "5": "Checkout",
    "6": "Exit"
}

SALES_TAX_RATE = 0.09
cart = {}

def display_menu():
    """Displays all menu item SKUs, names, and prices"""
    # Display menu header
    print("\n****Menu****\n")
    for sku in menu:
        # Slice the leading 'sku' string to retrieve the number portion
        parsed_sku = sku[3:]
        item = menu[sku]['name']
        price = menu[sku]['price']
        print("(" + parsed_sku + ")" + " " + item + ": $" + str(price))
        print("\n")  # Corrected newline character

def add_to_cart(sku, quantity=1):
    """
    Add an item and its quantity to the cart.
    
    :param string sku: The input SKU number to be ordered
    :param int quantity: The input quantity being ordered.
    """
    if sku in menu: 
        if sku in cart:
            cart[sku] += quantity
        else:
            cart[sku] = quantity
            print("Added", quantity, " of ", menu[sku]['name'], " to the cart.")
    else:
        print("I'm sorry. The menu number", sku, "that you entered is not on the menu.")

def remove_from_cart(sku):
    """
    Remove an item from the cart

    :param string sku: The input SKU number to remove from the cart
    """
    if sku in cart:
        removed_val = cart.pop(sku)
        print(f"Removed {menu[sku]['name']} from the cart.")
    else:
        print(f"I'm sorry, item with SKU {sku} is not currently in the cart.")

def modify_cart(sku, quantity):
    """
    Modify an item's quantity in the cart.

    :param string sku: The input SKU number being modified.
    :param int quantity: The input new quantity to use for the SKU.
    """
    if sku in cart:
        if quantity > 0:
            cart[sku] = quantity
            print(f"Modified {menu[sku]['name']} quantity to {quantity} in the cart.")
        else:
            # Call the previously defined function to remove a SKU from the cart
            remove_from_cart(sku)
    else:
        print(f"I'm sorry, item with SKU {sku} is not currently in the cart.")

def view_cart():
    """Display the menu item names, quantities, and prices inside the cart."""
    print("****Cart Contents****")
    subtotal = 0
    for sku in cart:
        quantity = cart[sku]
        price = menu[sku]["price"]
        item_total = price * quantity
        subtotal += item_total
        print(f"{quantity} x {menu[sku]['name']} (${price} each) = ${item_total:.2f}")
    tax = subtotal * SALES_TAX_RATE
    total = subtotal + tax
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}\n")
    

def checkout():
    """Display the subtotal information for the user to checkout"""
    print("****Checkout****")
    view_cart()
    print("Thanks for ordering!")
    print("*****")

def get_sku_and_quantity(sku_prompt, quantity_prompt=None):
    # Use the SKU prompt to get input from the user
    while True:
        item_sku = input(sku_prompt)
        # String concatenate "sku" to the beginning of the entered SKU number
        item_sku = "sku" + item_sku
        # If the quantity prompt is provided, get input from the user
        if quantity_prompt:
            # Use the quantity prompt to get input from the user
            quantity = input(quantity_prompt)
            # If the user typed a non-digit value, ask them to enter a valid quantity
            if not quantity.isdigit():
                print("Please enter a valid quantity (a positive integer).")
                continue
            quantity = int(quantity)
            return item_sku, quantity
        # Quantity prompt is None, meaning we do not need to get input for quantity
        else:
            return item_sku


def order_loop():
    """Loop ordering actions until checkout or exit"""
    # Display a welcome message to the user
    print("Welcome to the " + RESTAURANT_NAME + "!")
    # Set the conditional boolean variable that will be used to determine if the while loop
    # continues running or whether it should terminate
    ordering = True
    while ordering:
        # Display the app ordering actions
        print("\n****Ordering Actions****\n")
        for number in app_actions:
            description = app_actions[number]
            print("(" + number + ")", description)
        
        response = input("Please enter the number of the action you want to take: ")
        if response == "1":
            # User wants to order a menu item. Prompt them for SKU and quantity.
            display_menu()
            sku_prompt = "Please enter the SKU number for the menu item you want to order: "
            quantity_prompt = "Please enter the quantity you want to order [default is 1]: "
            ordered_sku, quantity = get_sku_and_quantity(sku_prompt, quantity_prompt)
            add_to_cart(ordered_sku, quantity)
        elif response == "2":
            # User wants to remove an item from the cart. Prompt them for SKU only.
            display_menu()
            sku_prompt = "Please enter the SKU number for the menu item you want to remove: "
            item_sku = get_sku_and_quantity(sku_prompt)
            remove_from_cart(item_sku)
        elif response == "3":
            # User wants to modify an item quantity in the cart. Prompt them for SKU and quantity.
            display_menu()
            sku_prompt = "Please enter the SKU number for the menu item you want to modify: "
            quantity_prompt = "Please enter the quantity you want to change to [default is 1]: "
            item_sku, quantity = get_sku_and_quantity(sku_prompt, quantity_prompt)
            modify_cart(item_sku, quantity)
        elif response == "4":
            # User wants to view the current cart contents. No user input needed.
            view_cart()
        elif response == "5":
            # User wants to checkout. No user input needed. Terminate the while loop after displaying.
            checkout()
            ordering = False
        elif response == "6":
            # User wants to exit before ordering. No user input needed. Terminate the while loop.
            print("Goodbye!")
            ordering = False
        else:
            # User has entered an invalid action number. Display a message.
            print("You have entered an invalid action number. Please try again.")
        

order_loop()

