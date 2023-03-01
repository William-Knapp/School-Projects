#!/usr/bin/env python3

#William Knapp
#COP2002.001
#Project 2 - program that takes the sum of odd/even numbers entered by the user

print("Sums of odd and even numbers")
print("==========================================")

choice = "y"
while choice.lower() == "y":

    numGood = False
    num = float(input("Enter a whole number between 1 and 50: "))

    while numGood == False:
        if ((not(int(num) == num)) or not(1 <= num <= 50)):
            num = float(input("Try again. Your number must be a whole number between 1 and 50: "))
        else:
            numGood = True
            num = int(num)

    isOdd = (num % 2)
    if (isOdd == 1):
        print("Your number is an odd number")
        
        oddSum = 0
        for x in range(1, num, 2):
            oddSum += x
        print("The sum of the odd numbers from 1 to", num, "is :", (oddSum + num))
        
    else:
        print ("Your number is an even number")

        evenSum = 0
        for x in range(0, num, 2):
            evenSum += x
        print("The sum of the even numbers from 0 to", num, "is :", (evenSum + num))

    choice = input("Try again? (y/n): ")

print("Bye!")
input("Press any button to quit...")
    
