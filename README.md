# Compound Word Segregation Program

## Overview
This program identifies compound words within a given text file(`Input_01.txt` and `Input_02.txt`). A compound word is defined as one that can be split into two or more smaller words present within the same list. The program also finds the largest and second-largest compound words in terms of character length. For efficiency, it utilizes memoization to store results of previously evaluated words, which helps reduce redundant calculations. 

## Design Decisions and Approach
1. **Input Handling**: The input file (`Input_01.txt` or `Input_02.txt`) is read and split into individual words, which are processed to identify compound words.
  
2. **Compound Word Identification**: The main function, `is_compound_word`, uses a recursive approach with memoization. For each word, it checks if it can be split into a prefix and a suffix such that both are present in the word list. The memoization dictionary (`memo`) stores the results of evaluated words to avoid re-evaluating them.

3. **Efficiency**: By storing words in a set (`words_set`), we achieve average constant-time complexity when checking for word existence, making the compound-word identification process faster. Memoization also helps to reduce redundant recursive calls.

4. **Output**: The program outputs the compound words identified, along with the largest and second-largest compound words. It also displays the total processing time.

## Execution Steps
This code identifies compound words from a list of words in the file `Input_01.txt` or `Input_02.txt`, separating them from simple words. It first reads words from the file and splits them into a list. The function `segregate_compound_words` then checks each word to see if it can be formed by combining two or more words from the list, marking such words as compound. The helper function `is_compound_word` uses recursion and memoization to efficiently determine if a word is compound by breaking it into prefixes and suffixes. Compound words and simple words are stored in separate lists. Finally, the code identifies the largest and second-largest compound words by length, prints them, and displays the processing time.


This program efficiently segregates compound words using recursive splitting with memoization, making it suitable for handling large datasets.
