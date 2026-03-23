#============================================================================
#                                 PHASE - 1                                 #
#============================================================================


import string as st


# Getting the text data from the user in text form or by manually typing
def get_text_data():
    with open("F:\Innomatics\Projects\Personal\Text_Alalyzer\Sample_Texts\sample_01.txt") as file:
        text_data = file.read()
    
    if text_data == "":
        user_text_data = input("Enter Your text Here:\n")
        return user_text_data
    return text_data


# Calculating the word count
def get_character_count(texts):
    specials = st.punctuation
    whitespace = st.whitespace

    with_special_chars = len(texts)
    without_special_chars = 0

    for i in texts:
        if i not in specials and i not in whitespace:
            without_special_chars += 1
    
    return with_special_chars,without_special_chars

# Calculating the word Count
def get_word_count(texts):
    if texts == "":
        return 0
    words = texts.split()
    word_count = len(words)
    return word_count
    

# Calculating the sentence count
def get_sentence_count(texts):
    if texts == "":
        return 0
    splitted_sentences = texts.replace(".","|").replace("!","|").replace("?","|").split("|")
    splitted_sentences = [s.strip() for s in splitted_sentences if s.strip()]
    return splitted_sentences,len(splitted_sentences)

# Calculating the Digit count
def get_digit_count(texts):
    if texts == "":
        return 0
    digit_count = 0
    for i in texts:
        if i.isdigit():
            digit_count += 1
    return digit_count

# Calculating the Avg Word length
def get_avg_word_length(texts):
    if texts == "":
        return 0
    words = texts.split()
    word_length = []
    for word in words:
        word_length.append(len(word))
    return round((sum(word_length) / len(word_length)),2)



# Calculating Avg Sentence Length
def get_avg_word_in_sentence_length(texts):
    if texts == "":
        return 0
    sentence,sentence_count = get_sentence_count(texts)
    word_count = 0
    for i in sentence:
        x = i.split(" ")
        word_count += len(x)
    avg_word_sen = word_count / len(sentence)
    return round(avg_word_sen,2)
