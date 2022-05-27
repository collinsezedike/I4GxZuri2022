# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    word = word.lower().replace(" ", "")
    anagram = anagram.lower().replace(" ", "")
    
    if all(letter in word for letter in anagram) \
        and all(letter in anagram for letter in word):
        return True
    else:
        return False
