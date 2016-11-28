def is_correct(dictionary, word):
    """ (Open File for reading, str) -> bool
    
    Return True iff word is a correctly-spelled word in dictionary.
    Note: due to a PCRS-specific constraint, the example calls below use Open with a capital 'O'.
    The actual function has a lowercase 'o'.
    
    >>> dict1 = Open('dict.txt', 'r')
    >>> is_correct(dict1, "Zyrtec")
    True
    >>> dict1.close()

    >>> dict1 = Open('dict.txt', 'r')
    >>> is_correct(dict1, "lolz")
    False
    >>> dict1.close()
    """
    for line in dictionary:
        if line.strip() == word:
            return True
    return False
    