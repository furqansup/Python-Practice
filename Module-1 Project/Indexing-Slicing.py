# You want to narrow down the list to the last 6 characters in the list. These characters are:

# Namor
# Doctor Strange
# Wolverine
# Captain America
# Black Widow
# Thor

# Write a code to slice these characters from the list

marvel_words = ['Avengers', 'X-Men', 'Spider-Man', 'Iron Man', 'Hulk', 'Thor', 'Black Widow', 'Captain America', 'Wolverine', 'Doctor Strange', 'Namor']

# Replace x with appropriate values
new_marvel = marvel_words[-6:]
print(new_marvel)

#Your code here
iron_man=marvel_words[3]
reversed_man=iron_man[::-1]
print(reversed_man)

spider_man=marvel_words[2] # Add appropriate index number
spidey_sliced=spider_man[0:6] # Add appropriate index number
print(spidey_sliced)