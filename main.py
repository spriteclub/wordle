from words import *

all_words = get_word_list()

words = []

for word in all_words:
    if 'r' in word: continue
    if 's' in word: continue
    if 'l' in word: continue
    if 'c' in word: continue
    
    if word[0] != 'a': continue
    if word[2] != 'o': continue
    if word[3] != 'n': continue
    if word[4] != 'e': continue
    words = words + [word]



freq = count_letter_frequency(words)

max_score = 0

for w in words:
    s = score(w, freq)
    if (s > max_score):
        max_score = s
        max_word = w

print(max_word)
print(max_score)
