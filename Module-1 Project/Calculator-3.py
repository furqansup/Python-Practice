class Calculator:
    def add (self, num1, num2):
        return num1 + num2
    
    def sub (self, num1, num2):
        return num1 - num2
    
    def mul (self, num1, num2):
        return num1 * num2
    
    def div (self, num1, num2):
        if num1 == 0:
            return ValueError("Cannot divide by Zero")
        else:
            return num1 / num2
        

calculation = Calculator()

print("Addition:", calculation.add(10, 20))
print("Subtraction:", calculation.sub(10, 20))
print("Multiplication:", calculation.mul(10, 20))
print("Division:", calculation.div(10, 20))