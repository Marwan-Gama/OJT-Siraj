"""
• Write a program to output the 100 words most frequently used in the Moby-Dick.txt by storing a count of each word
encountered in a dictionary
"""

from collections import Counter
import re

# Read the content of the Moby-Dick.txt file with UTF-8 encoding
with open('Moby-Dick.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Split text into words and convert them to lowercase
words = re.findall(r'\b\w+\b', text.lower())

# Count the occurrences of each word using Counter
word_count = Counter(words)

# Get the 100 most common words
most_common_words = word_count.most_common(100)

# Display the 100 most common words and their counts
for word, count in most_common_words:
    print(f'{word}: {count}')
