# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
"""Utilities for basic list statistics."""

from typing import List


# Function to calculate the sum
def calculate_sum(numbers: List[float]) -> float:
    """Return the sum of a list of numbers."""
    total = 0.0
    for num in numbers:
        total += num
    return total


# Function to calculate the average
def calculate_average(numbers: List[float]) -> float:
    """Return the average of a list of numbers.

    Raises ZeroDivisionError if numbers is empty.
    """
    total = calculate_sum(numbers)
    return total / len(numbers)


# Function to find the maximum number
def find_max(numbers: List[float]) -> float:
    """Return the maximum value from a list of numbers."""
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


# Function to find the minimum number
def find_min(numbers: List[float]) -> float:
    """Return the minimum value from a list of numbers."""
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


# Main program
def _main() -> None:
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: please enter an integer for N.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    nums: List[float] = []
    for i in range(n):
        try:
            number = float(input(f"Enter number {i + 1}: "))
        except ValueError:
            print("Invalid number, try again.")
            return
        nums.append(number)

    print("\nResults:")
    print("Sum:", calculate_sum(nums))
    print("Average:", calculate_average(nums))
    print("Maximum:", find_max(nums))
    print("Minimum:", find_min(nums))


if __name__ == "__main__":
    _main()

