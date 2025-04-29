# Here is an example of the list of dictionaries
stocks = [
    {'name': 'Apple Inc.', 'ticker': 'AAPL', 'price': 120.0, 'change': 0.05},
    {'name': 'Microsoft Corporation', 'ticker': 'MSFT', 'price': 95.0, 'change': -0.02},
    {'name': 'Amazon.com, Inc.', 'ticker': 'AMZN', 'price': 250.0, 'change': 0.1},
    {'name': 'Alphabet Inc.', 'ticker': 'GOOGL', 'price': 110.0, 'change': 0.02},
    {'name': 'Facebook, Inc.', 'ticker': 'FB', 'price': 80.0, 'change': 0.03}
]

# Write your code here

# Create a list of dictionaries where there is only the name and price which is above 100 and change % is only positive.
new_stocks= [{'name':stock['name'], 'price':stock['price']} for stock in stocks if stock['price'] > 100 and stock['change'] > 0]
print(new_stocks)
