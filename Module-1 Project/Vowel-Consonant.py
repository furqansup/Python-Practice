names = ["Alice", "Bob", "Eve", "Charlie", "Ivy", "David", "Olivia", "Peter"]

vowel_names = []
consonant_names = []

vowels = ['A', 'E', 'I', 'O', 'U']

for name in names:
    # Check if the first character (capitalized) is a vowel
    if name[0].upper() in vowels:
        vowel_names.append(name)
    else:
        consonant_names.append(name)

print("Names starting with vowels:", vowel_names)
print("Names starting with consonants:", consonant_names)
