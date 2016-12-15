# write six more test cases alongside the first two (6 MARKS)

def sort_guesses(guess_list, answer):
    ''' (list of float, float) -> dictionary of {str: list of float}
    
    Return a new dictionaryionary where each item in guess_list appears as an item
    in one of the dictionaryionary's values lists:
    - each item less than answer is in a list associated with key 'low',
    - each item equal to answer is in a list associated with key 'correct', and
    - each item greater than answer is in a list associated with key 'high'.
    If there are no items associated with one of 'low', 'correct', or 'high',
    then that string should not appear as a key in the new dictionaryionary.
    
    Case #1: no guesses
    Case #2: one low guess
    Case #3: one high guess
    Case #4: one correct guess
    Case #5: multiple low guesses, none correct
    Case #6: multiple high guesses, none correct
    Case #7: multiple low guesses, some correct
    Case #8: multiple high guesses, some correct
    
    >>> sort_guesses([], 5.5)
    {}
    >>> sort_guesses([4.5], 6.0) == {'low': [4.5]}
    True
    >>> sort_guesses([7.0], 5.0) == {'high': [7.0]}
    True
    >>> sort_guesses([4.0], 4.0) == {'correct': [4.0]}
    True
    >>> sort_guesses([4.0, 3.0, 2.0], 5.0) == {'low': [4.0, 3.0, 2.0]}
    True
    >>> sort_guesses([4.0, 3.0, 2.0], 1.0) == {'high': [4.0, 3.0, 2.0]}
    True
    >>> sort_guesses([4.0, 3.0, 2.0], 4.0) == {'low': [3.0, 2.0], 'correct': [4.0]}
    True
    >>> sort_guesses([4.0, 3.0, 2.0], 2.0) == {'high': [4.0, 3.0], 'correct': [2.0]}
    True
    '''
    
    dictionary = {}
    for float in guess_list:
        if float > answer:
            if 'high' not in dictionary:
                dictionary['high'] = []
            dictionary['high'].append(float)
        elif float < answer:
            if 'low' not in dictionary:
                dictionary['low'] = []
            dictionary['low'].append(float)
        else:
            if 'correct' not in dictionary:
                dictionary['correct'] = []
            dictionary['correct'].append(float)
    return dictionary

if __name__ == '__main__':
    import doctest
    doctest.testmod()
