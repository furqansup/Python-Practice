# Enter start number: 100
# Enter end number: 150
# Enter digit to count: 5
# The digit 5 appears 6 times between 100 and 150.

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
digit = (input("Enter the digit to count: ")) # input as string to count easily

count = 0

for num in range(first, second+1):
    # count digit occurrences in each number
    count+= str(num).count(digit)


print(f"The digit {digit} appears {count} between {first} and {second}")