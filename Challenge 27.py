# Even Odd Number Sorter App

print("welcome Even Odd Number Sorter")

while True:

    num_string = input("\n\nEnter the list of numbers separated by commas: ").replace(" ", "")
    num_list = num_string.split(",")

    odd_num = []
    even_num = []

    for num in num_list:
        num = int(num)
        if num%2 == 0:
            even_num.append(num)
        elif num%2 != 0:
            odd_num.append(num)

        else:
            print("Something went wrong! please only enter numbers separated with commas")

    print("\nHere is the Odd numbers: ",end="")
    for num in odd_num:
        print(num, end=",")

    print("\nAnd here is the even numbers: ",end="")
    for num in even_num:
        print(num, end=",")

    if input("\n\nRun again Y/n: ").lower() == "n":
        quit("Closing...")
    else:

        continue