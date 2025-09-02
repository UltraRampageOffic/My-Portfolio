# Query: sentence = input("Enter a sentence ending with a period: ")\n\ncharCount = 0\nwordCount = 1\nvowelCount = 0\n\nvowels = 'aeiouAEIOU'\n\nfor c in sentence:\n    charCount += 1\n\n    if c in vowels:\n        vowelCount += 1\n\n    if c == ' ':\n        wordCount += 1\n\nprint("Characters:", charCount)\nprint("Words:", wordCount)\nprint("Vowels:", vowelCount)\n
# ContextLines: 1

No Results
sentence = input("Enter a sentence ending with a period: ")

charCount = 0
wordCount = 1
vowelCount = 0

vowels = 'aeiouAEIOU'

for c in sentence:
    charCount += 1

    if c in vowels:
        vowelCount += 1

    if c == ' ':
        wordCount += 1

print("Characters:", charCount)
print("Words:", wordCount)
print("Vowels:", vowelCount)
