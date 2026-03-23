from text_analysis import get_word_count,get_sentence_count,get_character_count,get_avg_word_length,get_avg_word_in_sentence_length,get_digit_count
from text_analysis_phase_2 import get_longest_word,get_smallest_word,get_unique_word_count,most_common_words
from character_analysis import count_spaces,count_vowel_consonants,count_special_characters,count_upper_lower_characters,most_common_character

def print_menu():
    print("=====================================")
    print("TEXT ANALYZER v1.0")
    print("=====================================\n")
    print("Main Menu:")
    print("1. Analyze Text from File")
    print("2. Analyze Text from User Input")
    print("3. Exit")

def print_text_analysis(texts):
    print("===== TEXT ANALYSIS RESULTS =====\n")
    print("📊 CHARACTER STATISTICS")

    with_spec,without_spec = get_character_count(texts)
    print("\tTotal Characters (with spaces):",with_spec)
    print("\tAlphanumeric Characters Only:",without_spec)
    print()

    print("📝 WORD STATISTICS")
    print("\tTotal Words:",get_word_count(texts))
    print(f"\tAverage Word Length: {get_avg_word_length(texts)} characters")
    print()
    print("📄 SENTENCE STATISTICS")

    sentences,sen_count = get_sentence_count(texts)
    print(f"\tTotal Sentences: {sen_count}")
    print(f"\tAverage Words per Sentence: {get_avg_word_in_sentence_length(texts)}")
    print()
    
    print("🔢 DIGIT STATISTICS")
    print(f"\tTotal Digits: {get_digit_count(texts)}")


def print_text_analysis_phase_2(texts):
    print()
    print("📝 PHASE 2: WORD ANALYSIS")

    longest_word,longest_word_length = get_longest_word(texts)
    print(f"\tLongest Word(s): {longest_word} ({longest_word_length} characters)")

    shortest_word, shortest_word_length = get_smallest_word(texts)
    print(f"\tShortest Word(s): {shortest_word} ({shortest_word_length} characters)")

    unique_word_count = get_unique_word_count(texts)
    print(f"\tUnique Words: {unique_word_count}")

    print("\tTop 5 Most Common Words:")
    top5 = most_common_words(texts)
    for i , (word,count) in enumerate(top5,1):
        print(f"\t{i}. {word} - {count} times")


def print_character_analysis_phase_3(texts):
    print()
    print("🔤 PHASE 3: CHARACTER & DIGIT ANALYSIS")

    vowel_count,consonant_count = count_vowel_consonants(texts)
    print(f"\tVowels: {vowel_count}")
    print(f"\tConsonants: {consonant_count}")

    upper_count,lower_count = count_upper_lower_characters(texts)
    print(f"\tUppercase Letters: {upper_count}")
    print(f"\tLowercase Letters: {lower_count}")

    special_count = count_special_characters(texts)
    print(f"\tSpecial Characters: {special_count}")

    space_count = count_spaces(texts)
    print(f"\tTotal Spaces: {space_count}")

    letter,letter_count = most_common_character(texts)
    print(f"\tMost Common Character: '{letter}' (appears {letter_count} times)")

