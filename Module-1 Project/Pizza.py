# Here are the example lists of toppings
pizza_toppings = ['mushroom', 'olive', 'tomato', 'pepperoni', 'onion', 'garlic']
burger_toppings = ['lettuce', 'cheese', 'mayonnaise', 'bacon', 'pickle', 'avocado']

# Write your code here

# Looping to each topping checking if the toppings has more than 5 charachters
filtered_toppings = [topping for topping in pizza_toppings + burger_toppings if len(topping) > 5]

print(filtered_toppings)