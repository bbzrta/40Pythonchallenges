print("Welcome to the right triangle solver app")

first_leg = float(input("\nWhat is the size of the first leg of your triangle: "))
second_leg = float(input("What is the size of the second leg of your triangle: "))

hypotenuse = ((first_leg**2) + (second_leg**2))**(1/2)
hypotenuse = round(hypotenuse, 2)
area = (first_leg * second_leg)/2

print("\nhypotenuse: \t"+str(hypotenuse))
print("Area: \t\t\t" + str(area))