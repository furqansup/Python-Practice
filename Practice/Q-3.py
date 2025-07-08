# Q3. Count vowels in a string

def count_vowel(word):

    vowel = 'aeiou'
    count = 0

    for w in word:
        if w in vowel:
            count = count + 1
    
    return count

print(count_vowel('Superman'))