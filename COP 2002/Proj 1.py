#!/usr/bin/env python3

#William W Knapp
#COP2002.001
#9.22.2021
#Area and Perimeter
#This program uses input from the user to calculte the area and
#perimeter of a rectangle

#Welcome statement, asking for name
name = input("Enter your name: ")
print("\nThe Area and Perimeter Program\n")

#Get length and width values
length = float(input("Please enter the length: "))
width = float(input("Please enter the width: "))

#Perform calculations
area = length * width
peri = length + width

#Print result of calculations
print("\nArea =", area)
print("Perimeter =", peri)

#Goodbye statement
print("\n", name, ", thank you for using this program!", sep='')
input("\n\nPress the <ENTER> key to continue...")
