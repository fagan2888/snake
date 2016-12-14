# complete the function body (6 MARKS)

def is_syllable(phoneme):
    ''' (str) -> bool
    
    Return True iff phoneme is a syllable
    '''
    
    return phoneme[-1] == '0'

def count_syllables(words_pronunciation):
    ''' (list of list of str) -> int
    
    Return the number of syllables in words_pronunciation
    >>> count_syllables([['N', 'OW1'], ['G', 'UW1', 'F', 'IY0']])
    3
    '''
    
    num = 0
    for word_sounds in words_pronunciation:
        for phoneme in word_sounds:
            if is_syllable(phoneme):
                num = num + 1
    return num