# main.py
from collections import Counter
import re

def filterLetters(input: str) -> str:
    return "".join([c for c in input if c.isalpha()])

def findNumberOfUpperCasedLetters(input: str) -> str:
    return len([c for c in input if c.isupper()])

def findMostFrequentLetter(counterDict: {str: int}) -> int:
    return max(counterDict.values())
        
def findLongestWord(wordsList: [str]) -> str:
    return max(wordsList, key=len)

sentence = input("Enter a sentence: ").replace(".", "").replace(",", "")
words = sentence.split(" "); words.sort()
sentence = filterLetters(sentence).replace(" ", "")
upperLetters = findNumberOfUpperCasedLetters(sentence)
sentence = sentence.lower()

count = Counter(sentence)

# different letters
print(len(count))

# vowels
print(count["a"] + count["e"] + count["i"] + count["o"] + count["u"])

# Number of Upper Cased Letters
print(upperLetters)

# Most Frequent Letter
print(findMostFrequentLetter(count))

# Longest Word
print(findLongestWord(words))