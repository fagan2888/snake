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

def build_rhyming_dict(words_to_phonemes):
    # complete the function body (7 MARKS)
    ''' (dict of {str: list of str}) -> dict of {str: list of str}
    
    Return a dict where the keys are the same as the keys in word_to_phonemes
    and the value for each key is a list of all words that rhyme with the key.
    Two words rhyme if and only if they are different and their last
    vowel phonemes and all subsequent consonant phoneme(s) after the
    last vowel phonemes match.
    
    >>> words_to_phonemes = read_pronunciation(open('dictionary.txt'))
    >>> words_to_rhyming_words = build_rhyming_dict(words_to_phonemes)
    >>> words_to_rhyming_words['CRAIG']
    ['BAIG', 'BEGUE', 'FLAIG', 'HAGUE', 'HAIG', 'LAPHROAIG', 'MACIAG',
    'MCCAGUE', 'MCCAIG', 'MCKAIG', 'MCQUAIG', 'MCTAGUE',
    'NEST-EGG', 'O'LAGUE', 'PLAGUE', 'RAGUE', 'SPRAGUE', 'VAGUE']
    
    >>> # Notice that 'CRAIG' is not in the list of words that rhyme with 'CRAIG'
    '''
    
    # recall that two words rhyme iff their last vowel phonemes and
    # all subsequent consonant phonemes matched.
    
    words_to_rhyming_words = {}
    for word in words_to_phonemes:
        rhyming_words = []
        for potential_rhyme in words_to_phonemes:
            if (last_phonemes(words_to_phonemes[word]) == last_phonemes(words_to_phonemes[potential_rhyme])):
                rhyming_words.append(potential_rhyme)
        rhyming_words.remove(word)
        words_to_rhyming_words[word] = rhyming_words
    return words_to_rhyming_words

# suppose we had a solution which had a runtime which was quadratic in the
# length of the words_to_phonemes pythoin dict. If it took 1 second for
# build_rhyming_dict to run for a words_to_phonemes dict with 1000 words,
# then if we doubled the length to 2000 words, then we expect it to take
# 4 seconds, since if a = 1000, f(a) = 1 second, then f(2a) = (2^2) = 4