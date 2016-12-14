def remove_extra_spaces(s):
    ''' (str) -> str
    
    Return a string that is the same as s but with each group of multiple spaces
    replaced by a single space.
    
    >>> remove_extra_spaces('a    b')
    'a b'
    >>> remove_extra_spaces('   a  b c ')
    ' a b c '
    >>> remove_extra_spaces('    ')
    ' '
    >>> remove_extra_spaces('')
    ''
    '''
    single_space = ' ' # there is one space between these two quotes
    result = '' # there is no space between these two quotes
    i = 0
    
    while (i < len(s)):
        current_character = s[i]
        result = result + current_character
        i = i + 1
        if current_character == single_space:
            while (i < len(s) and s[i] == single_space):
                i = i + 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()