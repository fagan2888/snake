# write the function (6 MARKS)

def decode_message(secret_message, encoding):
    ''' (str, dict of {str: str} -> str
    
    Precondition: Message will only contain lowercase letters. No whitespace,
    digits or punctuation.
    
    >>> decode_message('abc', {'a': 'd', 'b': 'e', 'c': 'f'})
    'def'
    >>> decode_message('', {'a': 'd', 'b': 'e', 'c': 'f'})
    ''
    '''
    
    original_message = ''
    for char in secret_message:
        original_message += encoding[char]
    return original_message

if __name__ == '__main__':
    import doctest
    doctest.testmod()
