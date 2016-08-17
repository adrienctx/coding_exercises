"""
Question:Write a function to compute the Coleman-Liau readability score for a block of text:
CLI = 0.0588 * L - 0.296 * S - 15.8
L is the average number of letters per 100 words and S is the average number of sentences per 100 words.
"""
from __future__ import division


def get_coleman_liau_idx(text):
    """
    Here, we iterate through the text character by character. To count words, sentences and letters, we distinguish
    three cases: char is a sentence ending punctuation, char is a white space, and char is a letter.
    :param text: the text from which we want to compute the readability index
    :return: CLI, the index
    """

    # the variables used for counting
    nb_letters = 0
    nb_words = 0
    nb_sentences = 0

    # this keeps track of the length of the word we are currently iterating through
    # it is useful to identify acronyms (U.S.A., etc) and successive white space ('    ', etc)
    word_length = 0
    # this keeps track of the number of words in a sentence. It is useful to identify acronyms
    sentence_length = 0

    for i in range(len(text)):
        char = text[i]
        if char in ['.', '?', '!']:
            if i > 0 and (not text[i-1].isupper()) and sentence_length > 0:
                # If a sentence-ending punctuation is NOT preceded by an upper case letter,
                # and the sentence_length counter is at least 1 (i.e. there are at least 2 separate words in
                # the current sentence), this is a sentence end.
                nb_sentences += 1
                sentence_length = 0
                if word_length > 0:
                    # If there was an ongoing word (ending in lowercase), this is also this word's end
                    nb_words += 1
                    word_length = 0
        elif char in [' ', ':', ',', ';', '(', ')']:
            # only increment word count if finishing a word
            # (consecutive white spaces, and '.' + ' ' don't add words)
            # 'foobar,  ;   :::' only counts as 1 word
            if word_length > 0:
                nb_words += 1
                sentence_length += 1
                word_length = 0
        elif 96 < ord(char.lower()) < 123 or 47 < ord(char.lower()) < 58:
            nb_letters += 1
            word_length += 1

    # use the counts to compute the results
    L = 100 * nb_letters / nb_words
    S = nb_sentences * 100 / nb_words

    print(L, S, nb_words, nb_sentences, nb_letters)

    CLI = (0.0588 * L) - (0.296 * S) - 15.8

    return CLI
