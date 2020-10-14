

name = input("What is your name?")
print("Hello " + name.title() + "\nI will count the number times a letter will occurs in a message!")

message = input("Please Enter a message:").lower()
counter = input("What letter do you want me to count?").lower()
product = message.count(counter)
print(name.title() + ", your message has " + str(product) + " " + counter + "'s in it.")

print()
close = input("Press enter to exit.")

print("closing...")