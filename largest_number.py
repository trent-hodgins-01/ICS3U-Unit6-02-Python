# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/22/2021
# This is the list_array program
# The program generates and displays 10 random numbers between 1-100
# The program then figures out and displays the largest of the 10 numbers


import random


def largest_number(list_of_numbers):
    # this function determines the largest number i the array
    maximum = list_of_numbers[0]
    for x in list_of_numbers:
        if x > maximum:
            maximum = x

    return maximum


def main():
    # this function uses an array

    list_array = []
    answer = 0
    added_numbers = 0

    # input
    for loop_counter in range(0, 10):
        a_number = random.randint(1, 100)
        list_array.append(a_number)
        number = loop_counter + 1
        print("Random number {0} is {1}".format(number, a_number))
        added_numbers = added_numbers + a_number

    calculate = largest_number(list_array)

    print("\nThe largest number is {0}".format(calculate))

    print("\nDone.")


if __name__ == "__main__":
    main()
