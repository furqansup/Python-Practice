# Ask how many numbers to print
n = int(input("Enter how many Fibonacci numbers you want: "))

# Start with first two numbers
a = 0
b = 1

sequence = []

# Count how many numbers we’ve printed
count = 0

print("Fibonacci Sequence:")

while count < n:
    sequence.append(a)
    # Move to next number
    c = a + b
    a = b
    b = c
    count += 1

print(sequence)