# Factorial Calculator App
import math
# Welcome message for user
print("Welcome to Factorial Calculator App")

# Gathering Information
num1 = int(input("\nWhat number you like to compute the factorial of: "))

# Display the mathematical relationship
print("{0}! = ".format(num1), end=" ")
for i in range(1, num1):
    print(str(i), end="*")
print(num1)

# Using the math library
fact = math.factorial(num1)
print("\nThe result of the factorial based on the library is: ")
print("The factorial of {0} is {1}!".format(num1, fact))

# Using my own algorithm
fact2 = 1
for i in range(1, num1+1):
    fact2 = fact2*i
print("\nThe result of the factorial based on my own algorithm: ")
print("The factorial of {0} is {1}!".format(num1, fact2))

if fact == fact2:
    print("\nit is shown twice that {0}! = {1} (YAAY!)".format(num1, fact))
else:
    print("\nThere is something wrong with my algorithm!!")