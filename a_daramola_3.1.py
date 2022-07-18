#Akinola Daramola Jr
#Programming Exercise 3.1
#Due Date: 6/19/22


"""Write a program that asks the user for a number in the range of 1 through 7.
The program should display the corresponding day of the weekwhere
1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.
The program should display an error message if the user enters a number that is outside the range of 1 through 7.
"""

#Initialize value of variable
number = 0.0

#Declare value of variable
number = int(input("Input a number between 1 and 7. "))

#Conditional statements
if number == 1:
    print("Monday")
elif number == 2:
    print("Tueday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
#Error Message - number out of range
else:
    print("Error: Number is outside range of 1 and 7. Try again!")
    
