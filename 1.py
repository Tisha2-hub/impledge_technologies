import time
def is_compound_word(word, words_set, memo):
    if word in memo:
        return memo[word]
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in words_set and (suffix in words_set or is_compound_word(suffix, words_set, memo)):
            memo[word] = True
            return True
    memo[word] = False
    return False
def segregate_compound_words(words):
    words_set = set(words)
    compound_words = []
    simple_words = []
    memo = {}
    for word in words:
        if is_compound_word(word, words_set, memo):
            compound_words.append(word)
        else:
            simple_words.append(word)
    return compound_words, simple_words
with open('Input_01.txt', 'r') as file:
    words = file.read().split()
start_time = time.time()
compound_words, simple_words = segregate_compound_words(words)
if compound_words:
    largest = max(compound_words, key=len)
    compound_words.remove(largest)
    second_largest = max(compound_words, key=len) if compound_words else None
else:
    largest = None
    second_largest = None
end_time = time.time()
processing_time = end_time - start_time
print("Compound words found:")
for word in compound_words:
    print(word)
print(f"Largest compound word: {largest}")
print(f"Second largest compound word: {second_largest}")
print(f"Processing time: {processing_time} seconds")
