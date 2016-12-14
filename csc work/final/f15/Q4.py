def change_letters(word_list, char, position):
    # complete the body of the function (8 MARKS)
    ''' (list of str, str, int) -> NoneType
    
    Precondition: len(char) == 1 and position >= 0
    
    Modify word_list so that character char appears at index position of each
    item in the list. If position is not a valid index for a particular
    item, extend that string by filling all missing characters with char,
    up until the character at index position.
    
    >>> words = ['chocolate', 'milk']
    >>> change_letters(words, 's', 0)
    >>> words
    ['shocolate', 'silk']
    >>> words = ['abcd', 'efg', '']
    >>> change_letters(words, 'A', 4)
    >>> words
    ['abcdA', 'efgAA', 'AAAAA']
    '''
    
    for i in range(len(word_list)):
        if position > len(word_list[i]):
            difference = position - len(word_list[i])
            for j in range(difference):
                word_list[i] += char
        word_list[i] = word_list[i][:position] + char + word_list[i][position+1:]
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()