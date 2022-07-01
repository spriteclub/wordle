def get_word_list():
    # Start with an empty list
    words = []
    # Read the system dictionary.
    # Use the special 'with' keyword to close the file automatically at the end of the block.
    with open("/usr/share/dict/words", "r") as system_dictionary:
        # Loop through every line in the system dictionary file.
        for line in system_dictionary:
            # Each line contains one word.
            # Remove the trailing newline to get just the word.
            word = line.strip()
            # Skip any words that are not exactly 5 characters long.
            if len(word) != 5: continue
            # Skip any words that are not all lower case.
            if word.lower() != word: continue
            # If we get this far on this iteration of the loop, this word is good
            words.append(word)
    return words

def count_letter_frequency(words):
    letter_frequency = {}
    for word in words:
        for ch in word:
            if ch in letter_frequency:
                letter_frequency[ch] = letter_frequency[ch] + 1
            else:
                letter_frequency[ch] = 1
    return letter_frequency

        
word_list = get_word_list()
