fruit_list=['Mango','Mango','Mango','Pineapple','Pineapple','Pineapple','Apple','Mango','Banana','Apple',
            'Banana','Apple','Pineapple','Apple','Apple','Pineapple','Pineapple']

# Step 2: Create an empty dictionary which will contain the unique fruit names
fruit_dict={}

# Set the values for each key separately

# First Key
fruit_dict['Mango']= fruit_list.count("Mango")

# Second Key
fruit_dict['Pineapple']= fruit_list.count("Pineapple")

# Third Key
fruit_dict['Apple']= fruit_list.count("Apple")

# Fourth Key
fruit_dict['Banana']= fruit_list.count("Banana")

print (fruit_dict)