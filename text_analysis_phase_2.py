import string as st


def cleaning_word(texts):
    punctuations = st.punctuation
    words = texts.split()
    words = [word.strip(punctuations) for word in words]
    return words

# Longest word with its length
def get_longest_word(texts):
    if texts == "":
        return [],0
    
    words = cleaning_word(texts)

    longest_word = []
    longest_word_length = 0
    for word in words:
        if len(word) >  longest_word_length:
            longest_word = [word]
            longest_word_length = len(word)
        elif len(word) == longest_word_length:
            longest_word.append(word)
    return longest_word,longest_word_length


# Shortest Word with its length
def get_smallest_word(texts):
    if texts == "":
        return [], 0

    words = cleaning_word(texts)

    smallest_word = []
    smallest_word_length = float("inf")
    for word in words:
        if len(word) < smallest_word_length:
            smallest_word = [word]
            smallest_word_length = len(word)
        elif len(word) == smallest_word_length:
            if word not in smallest_word:
                smallest_word.append(word)
    return smallest_word,smallest_word_length


# Count Unique Word
def get_unique_word_count(texts):
    if texts == "":
        return 0
    words = cleaning_word(texts)
    unique_word_count = len(set(words))
    return unique_word_count

# List top 5 most common words
def most_common_words(texts):
    if texts == "":
        return []
    words = cleaning_word(texts)
    common_words = {}
    for word in words:
        if word in common_words:
            common_words[word] += 1
        else:
            common_words[word] = 1
    sorted_words = sorted(common_words.items(), key = lambda x:x[1], reverse=True)
    return sorted_words[:5]

