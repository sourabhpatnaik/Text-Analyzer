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

## How to Run
```
python main.py
```

## Project Structure
- `main.py` - Entry point
- `menu.py` - Menu and display functions
- `text_analysis.py` - Phase 1 analysis functions
- `text_analysis_phase_2.py` - Phase 2 analysis functions
- `sample_texts/` - Sample text files for testing

## Phase Progress
- [x] Phase 1: Basic Statistics
- [x] Phase 2: Word Analysis
- [ ] Phase 3: Character Analysis
- [ ] Phase 4: Search & Filter
- [ ] Phase 5: Advanced Features
- [ ] Phase 6: File Handling
- [ ] Phase 7: UI Improvements

## Technologies Used
- Python 3
- String module
- Data structures (lists, dictionaries, sets)

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
```