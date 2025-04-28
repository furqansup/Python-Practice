# Import reduce from functools module
from functools import reduce


# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Filter out even numbers (keep only odd)
odd = list(filter(lambda x : x % 2 !=0, numbers))

# Step 3: Square all the remaining odd numbers
odd_square = list(map(lambda x : x ** 2, odd))


# Step 4: Find the sum of all the squared odd numbers
sum_odd_squared = reduce(lambda x, y: x + y, odd_square)

# Step 5: Print the final result
print("Sum of squared odd numbers:", sum_odd_squared)