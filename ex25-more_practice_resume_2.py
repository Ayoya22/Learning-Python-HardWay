def break_words(stuffs):
    """"This is a simple function that will break words for us."""
    words = stuffs.split(' ')
    return words

def sort_words(words):
    """Sorts the words in a sentence or paragraph."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it of."""
    word = words.pop(-1)
    print(word)

