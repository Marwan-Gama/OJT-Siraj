
''''
• Anagrams are words that have the same number of same letters, but in different
• order. For instance:
• nap - pan
• ear - are - era
• cheaters - hectares – teachers
• Write a function clean_anagrams(words) that returns a list of words cleaned from anagrams
• For instance
'''


def clean_anagrams(words):
    # Create a dictionary to store sorted versions of words as keys and their original words as values
    anagram_dict = {}

    # Iterate through each word in the input list
    for word in words:
        # Sort the letters of the word to create a key for the dictionary
        sorted_word = ''.join(sorted(word))

        # If the sorted word is not in the dictionary, add it as a key with the original word as its value
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = word

    # Return the values (original words) from the dictionary
    return list(anagram_dict.values())


# Example usage:
word_list = ['nap', 'pan', 'ear', 'are', 'era', 'cheaters', 'hectares', 'teachers']
result = clean_anagrams(word_list)
print(result)
