#============================================================================
#                                 PHASE - 3                                 #
#============================================================================

import string as st

# Function for getting the All the SPACES in OUR TEXT
def count_spaces(texts):
    if texts == "":
        return 0
    return texts.count(" ")


# Function for calculating the Upper/Lower Case Characters
def count_upper_lower_characters(texts):
    if texts == "":
        return 0
    
    upper_char_count = 0
    lower_char_count = 0

    for char in texts:
        if char.isupper():
            upper_char_count += 1
        elif char.islower():
            lower_char_count += 1
    
    return upper_char_count,lower_char_count


# Function for Calculating the Vowels and Consonants in Our Text
def count_vowel_consonants(texts):
    if texts == "":
        return 0
    
    vowel_count = 0
    consonant_count = 0

    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    for char in texts:
        if char.lower() in vowels:
            vowel_count += 1
        elif char.lower() in consonants:
            consonant_count += 1
    
    return vowel_count,consonant_count


# Function to Count Special Characters
def count_special_characters(texts):
    special_chars = st.punctuation
    special_count = 0
    if texts == "":
        return 0
    
    for char in texts:
        if char in special_chars:
            special_count += 1
    
    return special_count


# Function to Count most common character
def most_common_character(texts):
    if texts == "":
        return 0

    char_freq = {}
    for char in texts:
        if char == " ":
            continue
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    most_common = max(char_freq.items(), key=lambda x:x[1])
    return most_common