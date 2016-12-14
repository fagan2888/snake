def organize_letters(message):
    # write six more test cases alongside the first two (6 MARKS)
    ''' (str) -> list of list of str
    Precondition: no uppercase letter appears more than once in
    message; no lowercase letter appears more than once in message.
    
    Return a list that contains two lists. Each lowercase letter from
    message appears as an item in the first list and each uppercase letter from
    message appears as an item in the second list. The letters should appear
    in the lists in the same order as they appear in message. Characters
    in message that are not letters do not appear in either list.
    Case #1: empty string
    Case #2: one lowercase letter
    Case #3: one uppercase letter
    Case #4: multi-character string, all lowercase letters
    Case #5: mutli-character string, all upercase letters
    Case #6: one non-letter
    Case #7: multiple non-letters
    Case #8: mix of uppercase, lowercase characters and non-letters
    >>> organize_letters('')
    [[], []]
    >>> organize_letters('a')
    [['a'], []]
    >>> organize_letters('A')
    [[], ['A']]
    >>> organize_letters('abcdefg')
    [['a', 'b', 'c', 'd', 'e', 'f', 'g'], []]
    >>> organize_letters('ABCDEFG')
    [[], ['A', 'B', 'C', 'D', 'E', 'F', 'G']]
    >>> organize_letters('!')
    [[], []]
    >>> organize_letters('!@#$%')
    [[], []]
    >>> organize_letters('@@@AB&&CDefg!!')
    [['e', 'f', 'g'], ['A', 'B', 'C', 'D']]
    '''
    
    lower_list = []
    upper_list = []
    
    for char in message:
        if char.isalpha():
            if char.isupper():
                upper_list.append(char)
            else:
                lower_list.append(char)
    return [lower_list, upper_list]

if __name__ == '__main__':
    import doctest
    doctest.testmod()