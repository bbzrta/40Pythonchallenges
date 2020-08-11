# Database Admin Program

print("Welcome to the Database Admin Program.")

# Dictionary for log in information.

login_info = {
    'moonman': 'password',
    'arsham': 'arshamjoon',
    'nickyD': 'world1star',
    'admin00': 'admin1234',
}
condition = "false"
while quit != "true":
    username = input("\nPlease enter you username: ")
    if username not in login_info.keys():
        retry_input = input("username not found! would you like to try again?(Y/n) ").lower().strip()
        if retry_input == "y":
            print("...")
        elif retry_input == "n":
            print("thanks for using our program. bye! ")
            break
        else:
            print("please enter a valid input!")
    elif username in login_info.keys():
        password = input("Please Enter your password: ")
        if password != login_info[username]:
            retry_input = input("Password not found! would you like to try again?(Y/n) ").lower().strip()
            if retry_input == "y":
                print("...")
            elif retry_input == "n":
                print("thanks for using our program. bye! ")
                break
            else:
                print("please enter a valid input!")

        elif password == login_info[username]:
            print("\nWelcome {0}! hope you are having a good day!".format(username))
            if username == "admin00":
                print("Here is your current database: ")
                for k, v in login_info.items():
                    print("\tUsername: {0} \tPassword: {1}".format(k, v))
            else:
                pass_change = input("Would you like to change your password? (y/n)")
                if pass_change == "y":
                    new_pass = input("\nWhat would you like your password to be? (minimum 8 characters.)")
                    if len(new_pass) >= 8:
                        login_info[username] = new_pass
                    else:
                        print("\n{0} is not the minimum 8 characters.".format(new_pass))
                    print("\nyour username is {0} and your password is {1}".format(username, login_info[username]))
                else:
                    print("\nThank you! goodbye!")
