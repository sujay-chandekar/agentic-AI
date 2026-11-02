def calculator(a, b, operation):
    if operation == "add":
        return a+b
    elif operation == "subtract":
        return a-b
    elif operation == "multiply":
        return a*b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a/b
    return "Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."