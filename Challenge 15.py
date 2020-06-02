# The Average Calculator App
print("Welcome to the Average Calculator App")

# Gathering Information
name = input("What is your name: ").title().strip()
grade_count= int(input("How many grades would you like to enter: "))
grades = []

# Loop for grade counter
for i in range(grade_count):
    grades.append(int(input("Enter grade: ")))

# Sorting Grades From highest to lowest and calculating average
grades.sort(reverse=True)
total = 0
for i in grades:
    total += i
average = total/grade_count
average = round(average, 2)
# Displaying Grades from highest to lowest one by one
print("\nGrades from Highest to Lowest: ")
for i in range(len(grades)):
    print("\t"+str(grades[i]))

# Displaying Grade Summary
print("\n{0}'s Grade Summary: ".format(name))
print("\tTotal Number of Grades: " + str(grade_count))
print("\tHighest Grade: " + str(grades[0]))
print("\tLowest Grade: " + str(grades[-1]))
print("\tAverage: " + str(average))

# Getting user inout for the second phase Calculations
desired_ave = int(input("\nWhat is you desired average: "))
difference = (desired_ave * (grade_count+1)) - total
difference = round(difference, 2)

print("\nGood luck {0}!".format(name))
print("For Getting the Desired Average you need "+ str(difference) + " for your next assignment.")

# ---------------Second Phase---------------

# making a copy of the list
grades2 = grades[:]

# asking for the wild dreams of the user
print("\nLets see what your average could have been if you did better/worse on an assignment.")

grades2.remove(int(input("What grade would you like to change: ")))
grades2.append(int(input("What grade would you like to get: ")))
grades2.sort(reverse=True)

average2 = sum(grades2)/len(grades2)

# Displaying Grades from highest to lowest one by one
print("\nNew grades from Highest to Lowest: ")
for i in range(len(grades)):
    print("\t"+str(grades2[i]))

# Displaying Grade Summary
print("\n{0}'s New Grade Summary: ".format(name))
print("\tTotal Number of Grades: " + str(grade_count))
print("\tHighest Grade: " + str(grades2[0]))
print("\tLowest Grade: " + str(grades2[-1]))
print("\tAverage: " + str(average2))

# Calculating the difference between the averages
changed = average2 - average
print("\nyour new average would be {0} compared to your real average of {1}".format(average2, average))
print("That is a change of {0} point!".format(changed))

print("\nToo bad your original grades are still the same!")
print(grades)
print("you should fo ask for some extra credit!")