while True:
    # Taking user input
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    operation = input("Enter the operation (addition, subtraction, multiplication, or division): ").lower()

    # Performing the selected operation
    if operation == "addition":
        result = num1 + num2
        print("Result:", result)

    elif operation == "subtraction":
        result = num1 - num2
        print("Result:", result)

    elif operation == "multiplication":
        result = num1 * num2
        print("Result:", result)

    elif operation == "division":
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation! Please choose from addition, subtraction, multiplication, or division.")

  