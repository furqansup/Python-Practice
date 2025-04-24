# List of numbers
numbers = [
    [2, 5, 11, 20, 8],
    [9, 4, 15, 28, 17],
    [1, 6, 21, 18, 3],
    [10, 13, 25, 33, 30],
    [14, 7, 16, 19, 22]
]

# Your code here:

# stone odd values
odd_num = []

# stone even values
even_num = []

for row in numbers:
    for num in row:
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)

print(f"Odd numbers counts: {len(odd_num)}")
print(f"Even numbers counts: {len(even_num)}")
