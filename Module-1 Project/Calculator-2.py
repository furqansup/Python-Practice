def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 -  num2
    elif operation == "*":
        return num1 *  num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid Operation"


result = calculator(10, 5, "&")
print(f"The result based upon the numbers and the operation is {result}")