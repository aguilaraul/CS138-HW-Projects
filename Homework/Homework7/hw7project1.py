#! /usr/bin/python
# File Name:     hw7project1.py
# Programmer:    Raul Aguilar
# Date:          June 20, 2020
#
# CS 138 1535 Homework 7 Project 1
# Write a program that takes as input the gender of the child, the
# height of the mother in inches and the height of the father in
# inches. Output the estimated adult height of the child in inches.
#
# Algorithm:
# 1. Ask if male or female child?
# 2. Enter height of mother in inches
# 3. Enter height of father in inches
# 4. Calculate estimated adult height using correct formula
# 5. Display result in inches and feet and inches
#

def main():
    validGenderEntry = False
    validMotherEntry = False
    validFatherEntry = False

    while not validGenderEntry:
        gender = input("Is the child male or female? ")
        if gender == "male" or gender == "female":
            validGenderEntry = True
        else:
            print("wrong gender")

    while not validMotherEntry:
        try:
            motherHeight = float(input("Enter the mother's height in inches: "))
            validMotherEntry = True
        except:
            print("\nInvalid height entered. Reenter height.\n")

    while not validFatherEntry:
        try:
            fatherHeight = float(input("Enter the father's height in inches: "))
            validFatherEntry = True
        except:
            print("\nInvalid height entered. Reenter height.\n")
    
    if(gender == "male"):
        childHeight = ((motherHeight*13/12)+fatherHeight)/2
    else:
        childHeight = ((fatherHeight*12/13)+motherHeight)/2

    feet = int(childHeight//12)
    inches = int(childHeight%12)

    print("\nThe estimated height as an adult is {:.2f} inches".format(childHeight), end="")
    print(" or {} feet and {} inches.".format(feet, inches))


main()