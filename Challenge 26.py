# Factor Generator App
print("Welcome to Factor Generator App!")

while True:

    user_num = int(input("what number would you like to see the factors for: "))
    factors = []

    # Finding the factors of the given number and appending them to a list.
    for i in range(1, user_num + 1):
        if user_num % i == 0:
            factors.append(i)

    print("Factors of {0} are:".format(user_num))

    for i in factors:
        print(i)

    print("\nThere are {0} factors for {1}!".format(len(factors), user_num))

    # Print a summary of the factors mathematically
    print("\nIn summary: ")
    for i in range(int(len(factors) / 2)):
        print(str(factors[i]) + " * " + str(factors[-i - 1]) + " = " + str(user_num))

    if input("\nRun again (Y/n): ") == "n":
        quit()
    else:
        continue
