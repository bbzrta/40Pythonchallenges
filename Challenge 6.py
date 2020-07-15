#information gathering
grades = []

grades.append(int(input("Please Enter your grade: ")))
grades.append(int(input("Please Enter your grade: ")))
grades.append(int(input("Please Enter your grade: ")))
grades.append(int(input("Please Enter your grade: ")))
print("Thanks")

#sorting the list
grades.sort(reverse=True)
print("\nYour Grades from highest to lowest are: " + str(grades))

#Removing the last two grades
removed_grade = grades.pop()
print("\nremoving grade " + str(removed_grade))
removed_grade = grades.pop()
print("removing grade " + str(removed_grade))

#remaining grades
print("\nyour remaining grades are :" + str(grades))
print("Nice job your highest grade is: " + str(grades[0]))


