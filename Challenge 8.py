#library required
import datetime
#variable list
shopping_list = ["Meat", "Cheese"]
purchased = []
#time conductor
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)


#Interface
print("\tWelcome to the Grocery List App")
print("The current date and time is: " + day + "/" + month + " \t " + hour + ":" + minute)
print("your currently have " + shopping_list[0] + " and " + shopping_list[1] + " in your list.")

#asking for more items
shopping_list.append(input("Type of food to add to the grocery list: ").title())
shopping_list.append(input("Type of food to add to the grocery list: ").title())
shopping_list.append(input("Type of food to add to the grocery list: ").title())


print("\nHere is grocery list:\n" + str(shopping_list))
shopping_list.sort()
print("Here is grocery list sorted: \n" + str(shopping_list))


#checking whats been purchased
print("\nSimulating grocery shopping...\n")

print("\nCurrent Grocery list: " + str(len(shopping_list)) + " items.")
print(shopping_list)
shopping_list.remove(input("What food did you just buy: ").title())

print("\nCurrent Grocery list: " + str(len(shopping_list)) + " items.")
print(shopping_list)
shopping_list.remove(input("What food did you just buy: ").title())

print("\nCurrent Grocery list: " + str(len(shopping_list)) + " items.")
print(shopping_list)
shopping_list.remove(input("What food did you just buy: ").title())

#Out of stock
print("Current Grocery list: " + str(len(shopping_list)) + " items.")
print(shopping_list)
no_item = shopping_list.pop()
print("\nSorry! we are out of " + no_item + ".")

shopping_list.insert(0, input("\nWhat food would you like intead: ").title())

print("\nHere is what remains in your list: \n")
print(shopping_list)