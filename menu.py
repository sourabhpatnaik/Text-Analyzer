from text_analysis import get_word_count,get_sentence_count,get_character_count,get_avg_word_length,get_avg_word_in_sentence_length,get_digit_count


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