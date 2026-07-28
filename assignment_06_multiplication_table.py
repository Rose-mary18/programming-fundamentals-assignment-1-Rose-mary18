# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.

# Part A: Display the multiplication table for one number
def single_table():
    number = int(input("Enter a number: "))

    if number <= 0:
        print("Error: Please enter a positive integer.")
        return

    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")


# Part B: Display multiplication tables from 1 to N
def tables_to_n():
    n = int(input("\nEnter a number N: "))

    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    for number in range(1, n + 1):
        print(f"\nMultiplication Table for {number}:")
        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")
        print("---------------------------")


# Main Program
print("PART A")
single_table()

print("\nPART B")
tables_to_n()

