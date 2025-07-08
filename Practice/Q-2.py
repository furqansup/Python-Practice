# Q2. Reverse a string

# method - 1 

def reverse_string( word ):

    rev_name = ""

    for i in range(len(word)-1, -1, -1):
        rev_name += word[i]

    return rev_name

print(reverse_string('Furqan'))


# method - 2

def slice_reversed (word):

    return word[::-1]

print(slice_reversed("Furqan"))

# method - 3

def reversed_word (word):

    rev_name = ""

    for i in reversed(word):
        rev_name += i
    
    return rev_name

print(reversed_word("Furqan"))

# method - 4

def prepending_reversed(word):

    rev_str = ''

    for i in word:
        rev_str = i + rev_str
    
    return rev_str

print(prepending_reversed('Furqan'))