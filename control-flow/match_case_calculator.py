# Function to perform the calculation based on the operation
def calculate(num1, num2, operation):
    match operation:
        case "add" | "+":
            return num1 + num2
        case "subtract" | "-":
            return num1 - num2
        case "multiply" | "*":
            return num1 * num2
        case "divide" | "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero is not allowed."
        case _:
            return "Invalid operation selected."

# Prompt the user to input numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to select an operation
operation = input("Choose the operation (+, -, *, /): ").lower()

# Perform the calculation
result = calculate(num1, num2, operation)

# Display the result
print(f"The result is: {result}")

