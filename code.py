#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sept 2019
# This is program for volume of square base pyramid 


def main():
    # funciton calculates circumference

    # welcome
    input( "This is the square-based pyramid volume calculator!")

    # input
    length = float(input("What is one side of the base:"))
    width = float(input("What is other side of the base:"))
    height = float(input("Finally, what is the height of the pyramid:"))

    # process
    volume = (length * width * height) / 3

    # output
    print("The volume is: " + str(round(volume)) + " units cubed.")


if __name__ == "__main__":
    main()