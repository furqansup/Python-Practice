# Here are the two lists
countries = ["USA", "Canada", "Mexico", "Brazil", "UK", "France", "Germany", "China", "India"]
sales = [2500, 300, 1200, 800, 500, 2000, 4000, 1000, 1500]

# Write your code here

sales_dict = {key : value for key, value in zip(countries, sales) if value > 1000}

print(sales_dict)