#!/usr/bin/env python3

"""
William Knapp
11/1/2021
COP 2002.001
Program takes integers from user, applies various calculations
to give the min, max, average, and median values of the data
"""

#function that gives the median value of a list with an odd number of elements
def odd_med(l, values):
    m = values[l//2]
    return m

#function that gives the median value of a list with an even number of elements
def even_med(l, values):
    mr = values[l//2]
    ml = values[(l//2) - 1]
    m = (mr+ml)/2
    return m


#function that prints the median, average, min, and max values
def output(m, total, l, values):
    print("The median value is:", m)
    print("The average value is:", (total/l))
    print("The minimum value is:", values[0])
    print("The maximum value is:", values[-1])


#main function
def main():

    choice = "y"

    while choice.lower() == "y":
        

        #initialize variables, print welcome message
        price = 0
        values = []
        total = 0
        print("          Real Estate Values")
        print("***************************************")

        #prompt user to input numbers into a list until -99 is entered
        while price != -99:
            price = int(input("Enter price of one home, or -99 to quit: "))
            if price == -99:
                break
            else:
                values.append(price)
                total += price

        #sorts values, prints list
        values.sort()
        print("***************************************")
        print("Prices of homes in your area:")
        print(values)
        print("***************************************")

        l = len(values)

        #decides which function to use based on parity of list
        if (l % 2):
            median = odd_med(l, values)
            

        else:
            median = even_med(l, values)

            
        #calls output function
        output(median, total, l, values)

        choice = input("\nContinue? (y/n): ")
        print()


#calls main function

if __name__ == "__main__":
    main()

input("\nPress <ENTER> key to quit...")
        

