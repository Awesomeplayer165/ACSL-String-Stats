# main.py
from collections import Counter

sentence = input("Enter a sentence: ").replace(" ", "")
count = Counter(sentence)

# different letters

print(len(count))

# vowels
print(count["a"] + count["e"] + count["i"] + count["o"] + count["u"])