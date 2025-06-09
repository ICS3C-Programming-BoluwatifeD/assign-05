#!/usr/bin/env python3
# Created By: Boluwatife Dada
# Date: May 22, 2025
# This program  Ask the user for the 3 sides of a triangle. Then calculate and display perimeter.


def calculate_triangle_perimeter():
    print("Greetings, from miles")
    """
    Asks the user for the three sides of a triangle,
    calculates the perimeter, and displays the result.
    """
    print("Let's calculate the perimeter of a triangle!")

    try:
        side1 = float(input("Enter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        side3 = float(input("Enter the length of side 3: "))
    except ValueError:
        print("Invalid input. Please enter numbers for the side lengths.")
        return

    # Basic check to ensure sides are positive
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Side lengths must be positive numbers.")
        return

    # Optional: Triangle Inequality Theorem check
    # This checks if the given sides can actually form a triangle
    if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
        print("These side lengths cannot form a valid triangle.")
        print("The sum of any two sides must be greater than the third side.")
        return

    perimeter = side1 + side2 + side3

    print(f"\nThe perimeter of the triangle is: {perimeter}")


# Call the function to run the program
calculate_triangle_perimeter()
