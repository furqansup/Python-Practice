try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = num1 / num2
    print("The result is:", result)

except ValueError:
    print("Invalid input! Please enter only numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero second number.")

except Exception as e:
    print("An unexpected error occurred:", e)
