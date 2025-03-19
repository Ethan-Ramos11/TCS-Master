def calculate(num1, num2, operation):
    """
    Perform a calculation on two numbers based on the specified operation.

    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation to perform ('+', '-', '*', '/')

    Returns:
        float: Result of the calculation

    Raises:
        ValueError: If operation is not supported
        ZeroDivisionError: If attempting to divide by zero
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        raise ValueError(f"Unsupported operation: {operation}")


def get_user_input():
    """
    Get input from the user for the calculator.

    Returns:
        tuple: (num1, num2, operation)

    Raises:
        ValueError: If input is not a valid number or operation
    """
    try:
        num1 = float(input("Enter first number: "))
        operation = input("Choose operation (+, -, *, /): ").strip()
        if operation not in {'+', '-', '*', '/'}:
            raise ValueError("Invalid operation")
        num2 = float(input("Enter second number: "))
        if operation == '/' and num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1, num2, operation
    except ValueError as e:
        raise ValueError("Please enter valid numbers and operation")


def main():
    """
    Main function to run the calculator program.
    """
    pass


if __name__ == "__main__":
    main()
