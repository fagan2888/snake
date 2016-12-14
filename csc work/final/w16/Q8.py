def build_poetry_assistant(words_to_phonemes):
    # complete the function body (8 MARKS)
    ''' (dict of {str: list of str}) -> dict of {tuple of str: list of str}
    
    Return a poetry assistant dictionary from the words to phonemes in
    words_to_phonemes.
    
    >>> word_to_phonemes = {'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'], 
    ...                     'OR': ['AO1', 'R']}
    >>> actual = build_poetry_assistant(words_to_phonemes)
    >>> expected = {('AH0',): ['THE', 'A'], ('AH0', M'): ['POEM'],
    ... ('AO1', 'R'): ['BEFORE', 'OR']}
    >>> actual == expected
    True
    '''
    
    rhyme_dict = {}
    for word in words_to_phomemes:
        # extract all phonemes for each key, as a tuple.
        end = tuple(last_phonemes(words_to_phonemes[word]))
        if end not in rhyme_dict:
            # insert an entry of the tuple in the dictionary
            rhyme_dict[end] = []
        # if word's values contains the tuple, append the word to the list.
        rhyme_dict[end].append(word)
    return rhyme_dict
    
def last_phonemes(phoneme_list):
    ''' (list of str) -> list of str
    
    Return the last vowel phoneme and any subequent consonant phoneme(s) from
    phoneme_list, in the same order as they appear in phoneme_list.
    
    >>> last_phonemes(['AE1', 'B', 'S', 'IH0', 'N', 'TH'])
    ['IH0', 'N', 'TH']
    >>> last_phonemes(['IH0', 'N'])
    ['IH0', 'N']
    '''
    vowels = 'AEIOU'
    last_phonemes_list = []
    candidate_phoneme = ''
    for i in range(len(phoneme_list)):
        if phoneme_list[i][0] in vowels:
            if phoneme_list[i] > candidate_phoneme:
                candidate_phoneme = phoneme_list[i]
    last_phonemes_list = phoneme_list[phoneme_list.index(candidate_phoneme):]
    return last_phonemes_list

def find_rhymes(phonemes_to_words, word):
    # complete the function body (4 MARKS)
    ''' (dict of {tuple of str: list of str}, str) -> list of str
    
    Precondition: word.isalpha() and word.isupper() are True, and word appears
    in exactly one value list in the phonemes_to_words dictionary
    
    Return a list of all words in phonemes_to_words that rhyme with word.
    Do not include word in the list.
    >>> phonemes_to_words = {('AO1', 'R'): ['BEFORE', 'OR'],
    ...                     ('AH0', 'M'): ['POEM'], ('AH0',): ['THE', 'A']}
    >>> find_rhymes(phonemes_to_words, 'OR')
    ['BEFORE']
    >>> find_rhymes(phonemes_to_words, 'POEM')
    []
    '''
    
    rhymes = []
    for phoneme in phonemes_to_words:
        if word in phonemes_to_words[phoneme]:
            for words in phonemse_to_words[phoneme]:
                if words != word:
                    rhymes.append[words]
    return rhymes
