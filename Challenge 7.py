#variables
str_list = ["10", "62", "73"]
int_list = [10, 62, 73]
float_list = [1.10, 2.20, 3.30]
list_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9,]]

print("\t\t\tSummary Table")

#String summary
print("\nThe variable str_list is a " + str(type(str_list)))
print("It contains the elements: " + str(str_list))
print("The element 10 is a " + str(type(str_list[0])))

#integer summary
print("\nThe variable int_list is a " + str(type(int_list)))
print("It contains the elements: " + str(int_list))
print("The element 10 is a " + str(type(int_list[0])))

#float summary
print("\nThe variable float_list is a " + str(type(float_list)))
print("It contains the elements: " + str(float_list))
print("The element 1.1 is a " + str(type(float_list[0])))

#List summary
print("\nThe variable list_list is a " + str(type(list_list)))
print("It contains the elements: " + str(list_list))
print("The element [1, 2, 3] is a " + str(type(list_list[0])))

#soritng lists
str_list.sort()
int_list.sort()

#outputing the sirted lists.
print("\nSorting str_list and int_list...")
print("Sorted str_list: " + str(str_list))
print("Sorted int_list: " + str(int_list))

#Finale
print("\nStrings are sorted alphabetically while integers are sorted numerically!")