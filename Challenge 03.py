print("Welcome to the temperature conversion app.")
fahrenheit = float(input("\nPlease Enter Your temperature in Fahrenheit: "))

fahrenheit = round(fahrenheit, 4)
celsius = (fahrenheit - 32)/1.8000
celsius = round(celsius, 4)
kelvin = (((fahrenheit - 32)*5)/9) + 273.15
kelvin = round(kelvin, 4)

print("Fahrenheit is:"   +"\t" + str(fahrenheit) +"F")
print("Celsius is:"      +"\t\t" + str(celsius) +"C")
print("Kelvin is:"       +"\t\t" + str(kelvin) +"K")


