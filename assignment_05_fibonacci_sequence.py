# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#

"""Simple statistics utilities: calculate sum/average and find max/min from user input."""

# Part 1: Find the sum and average of a list of numbers
def calculate_statistics() -> None:
    """Read a list of numbers from the user and print their sum and average."""
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: Number of values must be positive.")
        return

    numbers: list[float] = []
    total: float = 0.0

    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
        total += num

    average = total / n

    print("\nResults")
    print("Sum:", total)
    print("Average:", average)


# Part 2: Find the largest and smallest numbers
def find_max_min() -> None:
    """Read a list of numbers from the user and print the largest and smallest."""
    n = int(input("\nHow many numbers? "))

    if n <= 0:
        print("Error: Number of values must be positive.")
        return

    numbers: list[float] = []

    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    print("\nResults")
    print("Maximum:", maximum)
    print("Minimum:", minimum)


# Main Program
print("PART 1")
calculate_statistics()

print("\nPART 2")
find_max_min()



