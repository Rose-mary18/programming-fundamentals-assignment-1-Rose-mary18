"""Simple calculator application with basic arithmetic operations."""

from typing import Union


def addition(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtraction(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b


def multiplication(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def division(a: float, b: float) -> Union[float, str]:
    """Divide two numbers with zero-division check."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return round(a / b, 2)


def modulus(a: float, b: float) -> Union[float, str]:
    """Calculate modulus with zero-division check."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a % b


def exponentiation(a: float, b: float) -> float:
    """Raise a number to a power."""
    return a ** b


# Main Program
while True:
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

    choice = input("Select an operation (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Error: Invalid choice.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = addition(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")

    elif choice == "2":
        result = subtraction(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")

    elif choice == "3":
        result = multiplication(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")

    elif choice == "4":
        result = division(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(f"Result: {num1} / {num2} = {result}")

    elif choice == "5":
        result = modulus(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(f"Result: {num1} % {num2} = {result}")

    elif choice == "6":
        result = exponentiation(num1, num2)
        print(f"Result: {num1} ** {num2} = {result}")
