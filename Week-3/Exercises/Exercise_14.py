import string
from collections import Counter

'''
• Define a function count_words(text) that gets a text, and prints the list of words in the text with the number 
of occurrences of each word
• The words should be printed from the most common word to the least common word
• * Use Python’s string methods to strip out any punctuation (to replace any of the following characters: 
!?":;,()’.*[])
'''

def count_words(text):
    # Remove punctuation from the text
    for char in string.punctuation:
        text = text.replace(char, '')

    # Convert text to lowercase and split into words
    words = text.lower().split()

    # Count occurrences of each word
    word_counts = Counter(words)

    # Sort words by their counts in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the list of words with their counts
    for word, count in sorted_words:
        print(f"{word}: {count}",end=",")

# Example usage:
text_to_count = "Your input text goes here! This is an example text, with some punctuation."
count_words(text_to_count)
