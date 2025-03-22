# Simple Calculator with Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

def main():
    try:
        # Step 1: Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter the operation (+, -, *, /): ")

        # Step 2: Perform Calculation
        if operation == '+':
            result = add(num1, num2)
            print(f"\nStep: {num1} + {num2} = {result}")

        elif operation == '-':
            result = subtract(num1, num2)
            print(f"\nStep: {num1} - {num2} = {result}")

        elif operation == '*':
            result = multiply(num1, num2)
            print(f"\nStep: {num1} * {num2} = {result}")

        elif operation == '/':
            result = divide(num1, num2)
            print(f"\nStep: {num1} / {num2} = {result}")

        else:
            print("\nInvalid operation selected!")

    except ValueError:
        print("\nError: Please enter valid numeric values.")

if __name__ == "__main__":
    main()
