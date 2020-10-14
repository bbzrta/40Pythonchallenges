print("Welcome to MPS to MPH convertor Program.")
speed_miles = float(input("Please Enter yours speed in miles per hour: "))
speed_meters = speed_miles * 0.44704
speed_meters = round(speed_meters, 2)
print("Your speed is " + str(speed_meters) + " MPS.")
