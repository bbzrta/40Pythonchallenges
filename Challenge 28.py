# Prime Number App
print("Welcome to the Prime Number App.")

while True:
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")

    choice = input("\nEnter your choice 1 or 2:").strip()

    if choice == "1":
        num = int(input("\nEnter a number to determine if its prime or not: "))

        prime_status = True
        for i in range(2, num) :

            if num % i == 0 and num != i:
                prime_status = False
                break


        if prime_status:
            input("{0} is prime!".format(num))
        else:
            input("{0} is not prime!".format(num))




    elif choice == "2":
        low_num = int(input("Enter your lower number: "))
        high_num = int(input("Enter your higher number: "))

        primes = []

        for i in range(low_num, high_num + 1):
            for x in range(2, high_num+1):
                if i % x != 0 and x != i:
                    primes.append(i)

        print(primes)

