# Define sets for fruits in each basket
basket1 = {'apple', 'banana', 'grape', 'orange'}
basket2 = {'banana', 'mango', 'pineapple', 'orange'}

# Find the total number of fruits available
total_fruits = len(basket1.union(basket2))
print("Total number of fruits available:", total_fruits)

# Find fruits available in both baskets
both_baskets = basket1.union(basket2)    # Replace x with appropriate method
print("All the available fruits:", both_baskets)

# # Find only the common fruits in both baskets
common_fruits = basket1.intersection(basket2)   # Replace x with appropriate method
print("Common fruits in both baskets:", common_fruits)

# # Find fruits unique to each basket
unique_basket1 = basket1.difference(basket2)    # Replace x with appropriate method
unique_basket2 = basket2.difference(basket1)    # Replace x with appropriate method
print("Fruits unique to basket 1:", unique_basket1)
print("Fruits unique to basket 2:", unique_basket2)


