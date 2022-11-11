import string

# List of "unimportant" words
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would', 'old', 'young']


def filter_words(words, skip_words):
    """This function takes a list of words and returns a copy of the list from
    which all words provided in the list skip_words have been removed."""

    # return a list of the words that don't occur in skip_words, and it isn't an empty string'
    return [word for word in words if word not in skip_words and word]


def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The function takes a string and returns a new string
    which does not contain any punctuation."""

    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct


def normalise_input(user_input):
    """This function removes all punctuation from the string and converts it to
    lower case. It then splits the string into a list of words (also removing
    any extra spaces between words) and further removes all "unimportant"
    words from the list of words using the filter_words() function. The
    resulting list of "important" words is returned."""

    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()
    words = no_punct.split(' ')
    filtered_words = filter_words(words, skip_words)
    return filtered_words
