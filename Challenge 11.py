# Binary/Hexadecimal Converter App

# Printing Welcome Message
print("Welcome to the Binary/Hexadecimal Converter App!")

# Get user input and generate lists.
max_input = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))
decimal = list(range(1, max_input + 1))
binary = []
hexadecimal = []

for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
print("Generating the lists...")

# Slicing index from user
print("\nUsing slices, we will now show a portion of each list.")
lower_range = int(input("What Decimal number would you like to start at: "))
upper_range = int(input("What decimal number would you like to stop at: "))

# Slice through each list individually
print("\nDecimal values from " + str(lower_range) + " to " + str(upper_range) + ".")
for num in decimal[lower_range-1:upper_range]:
    print(num)

print("\nBinary values from " + str(lower_range) + " to " + str(upper_range) + ".")
for num in binary[lower_range - 1:upper_range]:
    print(num)

print("\nHexadecimal values from " + str(lower_range) + " to " + str(upper_range) + ".")
for num in hexadecimal[lower_range - 1:upper_range]:
    print(num)
# Output the whole list for the user to see
input("Press enter to see the whole list from 1 to " + str(max_input) + ".")
print("Decimal------Binary------Hexadecimal")
print("------------------------------------")
for d, b, h in zip(decimal, binary, hexadecimal):
    print(str(d) + "------" + str(b) + "------" + str(h))
