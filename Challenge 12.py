# For Loops Challenge 12: Quadratic Equation Solver App
import cmath

# Print Welcome Information
print("Welcome to the Quadratic Equation Solver App.")
print("\nA Quadratic Equation is of the form ax^2 + bx + c + 0")
print("Your solution can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion")


# Gathering Information
count = int(input("\nHow many equations would you like to solve today?"))
count = count + 1
# Doing the math
for i in range(1, count):
    print("\nSolving equation #" + str(i))
    print("-----------------------------------")
    num_a = float(input("Please Enter your value of 'a': "))
    num_b = float(input("Please Enter your value of 'b': "))
    num_c = float(input("Please Enter your value of 'c': "))
# calculate the discriminant
    d = (num_b**2) - (4*num_a*num_c)
# finding two solutions
    sol1 = (-num_b-cmath.sqrt(d))/(2*num_a)
    sol2 = (-num_b+cmath.sqrt(d))/(2*num_a)
# printing solutions
    print("\nthe solutions to {0}x^2 + {1}x + {2} + 0 are:".format(num_a, num_b, num_c))
    print("\nX1 = {0}\nX2 = {1}".format(sol1, sol2))

print("\nthank you for using quadratic equation solver app! bye..")