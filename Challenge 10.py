# Favourite Teachers Program
print("Welcome to the Favourite Teachers Program.\n")
teachers = []

# Gathering information from the user.
teachers.append(input("Who is Your first favourite teacher: "))
teachers.append(input("Who is Your second favourite teacher: "))
teachers.append(input("Who is Your third favourite teacher: "))
teachers.append(input("Who is Your fourth favourite teacher: "))

# Sorting and displaying the information.
print("\nYour favourite teachers ranked are: " + str(teachers))
print("Your favourite teachers alphabetically are: " + str(sorted(teachers)))
print("Your favourite teachers in reverse alphabetical order are: " + str(sorted(teachers, reverse= True)))
                    # Displaying them in couples.
print("\nYour top two favourite teachers are: " + str(teachers[0]) +" and " + str(teachers[1]))
print("Your next two favourite teachers are: " + str(teachers[2]) + " and " + str(teachers[3]))
print("Your last favourite teachers is: " + str(teachers[3]))
print("you have " + str(len(teachers)) + "favourite teachers")

# Replacing the favourite teacher.

teachers.insert(0, input("Oops," + str(teachers[0]) + " is no longer your favourite teacher. Who is your new favourite "
                                                      "teacher: "))
# Sorting and displaying the information.
print("\nYour favourite teachers ranked are: " + str(teachers))
print("Your favourite teachers alphabetically are: " + str(sorted(teachers)))
print("Your favourite teachers in reverse alphabetical order are: " + str(sorted(teachers, reverse= True)))
                    # Displaying them in couples.
print("\nYour top two favourite teachers are: " + str(teachers[0]) +" and " + str(teachers[1]))
print("Your next two favourite teachers are: " + str(teachers[2]) + " and " + str(teachers[3]))
print("Your last favourite teachers is: " + str(teachers[3]))
print("you have " + str(len(teachers)) + "favourite teachers")