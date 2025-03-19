#My simple program
def calculate(num1, num2, operation):
    """Perform the requested mathematical operation."""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero is not allowed."
    else:
        return "Invalid operation! Please use +, -, *, or /."

# Get user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ").strip()

    # Perform calculation
    result = calculate(num1, num2, operation)

    # Display result
    print(f"\nResult: {num1} {operation} {num2} = {result}")

except ValueError:
    print("Invalid input! Please enter numeric values for the numbers.")