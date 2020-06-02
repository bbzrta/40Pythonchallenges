# username data base
username = ["arsham", "majid", "hamid"]

# Welcome message
print("Welcome to the Shipping Accounts Program.")

# Asking for the username
userinput = input("Hello, what is your username?").strip()


if userinput in username:
    print("hello {0}. Welcome back to your account.".format(userinput))
    print("\nShipping orders 0 to 100:\t\t\t$5.10 each")
    print("Shipping orders 100 to 500:\t\t\t$5.00 each")
    print("Shipping orders 500 to 1000:\t\t\t$4.95 each")
    print("Shipping orders over 1000:\t\t\t$4.80 each")

    shipment_count = int(input("How many items would you like to ship: "))
    if shipment_count < 100:
        shipment_cost = 5.10
    elif shipment_count < 500:
        shipment_cost = 5.00
    elif shipment_count < 1000:
        shipment_cost = 4.95
    else:
        shipment_cost = 4.80

    shipment_cost = round(shipment_cost, 2)
    shipment_final = shipment_cost*shipment_count
    shipment_final = round   (shipment_final, 2)
    print("To ship {0} items it will cost you ${1} at ${2} per item.".format(shipment_count, shipment_final, shipment_cost))

    yesno = input("would you like to place this order (y/n):").lower
    if yesno == "y":
        print("Okay. Shipping your {0} items.".format(shipment_count))
    else:
        print("Okay. no order is being placed at this time.")

else:
    print("Sorry, you dont have an account with us. Goodbye.")

