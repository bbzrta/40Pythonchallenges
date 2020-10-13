# Factor Generator App
print("Welcome to Factor Generator App!")
user_num = int(input("what number would you like to see th factors for: "))

end = False

while not end:

    factors = []

    # Finding the factors of the given number and appending them to a list.
    for i in range(1, user_num):
        if user_num % i == 0:
            factors.append(i)

    
    print("Factors of {0} are:".format(user_num))
    
    for i in factors:
        print(int(i))










    user_ender = input("would you like to try another number?")
    if user_ender == "n":
        end = True