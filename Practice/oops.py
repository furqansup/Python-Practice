# class Employee:
#     def set_details(self, name, salary):
#         self.name=name
#         self.salary=salary



# emp1 = Employee().set_details('furqan', 27)
# epm2 = Employee()

# print (emp1)

# Make a calculator:

num1= 10
num2= 0

class Calculator:
    def add(x, y):
        return f"Addition Result: {x+y}"
    
    def sub(x, y):
        return f"Subtraction Result: {x-y}"
    
    def mul(x, y):
        return f"Multiplication Result: {x*y}"
    
    def div(x, y):
        if y==0:
            return "Division Result: Error: Division by zero is not allowed."
        else:
            return f"Multiplication Result: {x/y}"
        

class Result:
    def calculate(a, b):
        print(Calculator.add(a, b))
        print(Calculator.sub(a, b))
        print(Calculator.mul(a, b))
        print(Calculator.div(a, b))

Result.calculate(num1, num2)

class test:
     def __init__(self,a="Hello World"):
         self.a=a
 
     def display(self):
         print(self.a)
obj=test()
obj.display()

