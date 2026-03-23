# Text Analyzer 📝

A Python-based command-line text analysis tool that provides comprehensive statistics about your text. Analyze text files or user input to get insights on character counts, word frequency, sentence structure, and more!

## Features

### Phase 1: Basic Statistics ✅
- Character count (with/without spaces)
- Word count
- Sentence count
- Digit count
- Average word length
- Average sentence length

### Phase 2: Word Analysis ✅
- Longest word detection
- Shortest word detection
- Unique word count
- Top 5 most common words with frequency

### Phase 3: Character & Digit Analysis ✅
- Vowels vs consonants count
- Uppercase vs lowercase letters
- Special characters count
- Total spaces count
- Most common character detection

## How to Run
```
python main.py
```

## Project Structure
- `main.py` - Entry point
- `menu.py` - Menu and display functions
- `text_analyzer.py` - Phase 1 analysis functions
- `text_analysis.py` - Phase 2 analysis functions
- `character_analysis.py` - Phase 3 analysis functions
- `file_handler.py` - File reading and input handling
- `sample_texts/` - Sample text files for testing

## Phase Progress
- [x] Phase 1: Basic Statistics
- [x] Phase 2: Word Analysis
- [x] Phase 3: Character Analysis
- [ ] Phase 4: Search & Filter
- [ ] Phase 5: Advanced Features
- [ ] Phase 6: File Handling
- [ ] Phase 7: UI Improvements

## Technologies Used
- Python 3
- String module
- Data structures (lists, dictionaries, sets)
- Lambda functions for sorting

## Example Output
```
===== TEXT ANALYSIS RESULTS =====

📊 CHARACTER STATISTICS
    Total Characters (with spaces): 100
    Alphanumeric Characters Only: 85

📝 WORD STATISTICS
    Total Words: 18
    Average Word Length: 4.72 characters

📄 SENTENCE STATISTICS
    Total Sentences: 2
    Average Words per Sentence: 9.0

🔢 DIGIT STATISTICS
    Total Digits: 5

📝 PHASE 2: WORD ANALYSIS
    Longest Word(s): ['analysis'] (8 characters)
    Shortest Word(s): ['a'] (1 character)
    Unique Words: 16
    Top 5 Most Common Words:
        1. text - 3 times
        2. analysis - 2 times
        3. word - 2 times

🔤 PHASE 3: CHARACTER & DIGIT ANALYSIS
    Vowels: 32
    Consonants: 53
    Uppercase Letters: 3
    Lowercase Letters: 82
    Special Characters: 8
    Total Spaces: 17
    Most Common Character: 'a' (appears 6 times)
```

## Functions Overview

### Phase 1: text_analyzer.py
```python
get_text_data()                           # Get text from file or user input
get_character_count(text)                 # Count characters
get_word_count(text)                      # Count total words
get_sentence_count(text)                  # Count total sentences
get_digit_count(text)                     # Count digits
get_avg_word_length(text)                 # Calculate average word length
get_avg_word_in_sentence_length(text)     # Calculate average words per sentence
```

### Phase 2: text_analysis.py
```python
cleaning_word(text)                       # Helper function to clean punctuation
get_longest_word(text)                    # Find longest word(s)
get_smallest_word(text)                   # Find shortest word(s)
get_unique_word_count(text)               # Count unique words
most_common_words(text)                   # Get top 5 most common words
```

### Phase 3: character_analysis.py
```python
count_spaces(text)                        # Count total spaces
count_upper_lower_characters(text)        # Count uppercase and lowercase letters
count_vowel_consonants(text)              # Count vowels and consonants
count_special_characters(text)            # Count special characters
most_common_character(text)               # Find most common character
```

## Skills Demonstrated

✅ Procedural Python programming
✅ String manipulation and text processing
✅ Data structures (lists, dictionaries, sets)
✅ Functions and modular code design
✅ Loops and conditional logic
✅ File I/O operations
✅ Lambda functions and sorting
✅ CLI design and user interaction
✅ Character-level text analysis
✅ Frequency counting and ranking

## Development Progress

**Total Functions:** 17/40+
**Total Phases Complete:** 3/7
**Code Quality:** Professional & Modular
**Resume Ready:** ✅ Yes

## Upcoming Phases

- **Phase 4:** Search & filter features (find words, substring matching)
- **Phase 5:** Advanced features (reading time, sentiment, palindromes)
- **Phase 6:** File handling & reports (export results, batch processing)
- **Phase 7:** Enhanced UI & polish (better navigation, performance)

## Testing

Test the application with various inputs:
- Empty text
- Text with special characters
- Text with numbers and digits
- Text with mixed case letters
- Large text files

## Author

**Sourabh**
- Location: Hyderabad, India
- Learning: Data Science at Innomatics Research Lab

## License

This project is open source and available under the MIT License.

---

**Status:** Active Development 🚀
**Progress:** 43% Complete (3/7 phases)
**Last Updated:** March 2026