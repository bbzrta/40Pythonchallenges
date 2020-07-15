print("Welcome to the Multiplication/Exponent Table App")

#gathering information
name = input("What's your name?").strip().title()
num = float(input("Please Enter your number: "))
message = ("Math is cool!")

#multiplication table is here:
print("\n\tMultiplication Table for " + str(num))
print("\n\t1.0 x " + str(num) + " = " + str(round(1*num, 4)))
print("\t2.0 x " + str(num) + " = " + str(round(2*num, 4)))
print("\t3.0 x " + str(num) + " = " + str(round(3*num, 4)))
print("\t4.0 x " + str(num) + " = " + str(round(4*num, 4)))
print("\t5.0 x " + str(num) + " = " + str(round(5*num, 4)))
print("\t6.0 x " + str(num) + " = " + str(round(6*num, 4)))
print("\t7.0 x " + str(num) + " = " + str(round(7*num, 4)))
print("\t8.0 x " + str(num) + " = " + str(round(8*num, 4)))
print("\t9.0 x " + str(num) + " = " + str(round(9*num, 4)))


#Exponent Table
print("\n\tExponent Table for "+ str(num))
print("\n\t" + str(num) + " ** 1 " + " = " + str(round(num**1, 4)))
print("\t" + str(num) + " ** 2 " + " = " + str(round(num**2, 4)))
print("\t" + str(num) + " ** 3 " + " = " + str(round(num**3, 4)))
print("\t" + str(num) + " ** 4 " + " = " + str(round(num**4, 4)))
print("\t" + str(num) + " ** 5 " + " = " + str(round(num**5, 4)))
print("\t" + str(num) + " ** 6 " + " = " + str(round(num**6, 4)))
print("\t" + str(num) + " ** 7 " + " = " + str(round(num**7, 4)))
print("\t" + str(num) + " ** 8 " + " = " + str(round(num**8, 4)))
print("\t" + str(num) + " ** 9 " + " = " + str(round(num**9, 4)))

#Math is cool
print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.upper())