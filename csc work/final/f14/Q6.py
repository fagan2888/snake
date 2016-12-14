def replace_items(L, D):
    # complete the function body (3 MARKS)
    ''' (list of int, dict of {int: int}) -> NoneType
    
    Some of the items in L may be keys in D. Replace those items with the
    associated values in D.
    
    >>> L = [1]
    >>> replace_items(L, {1: 2})
    >>> L
    [2]
    >>> L = [3]
    >>> replace_items(L, {1: 2})
    >>> L
    [3]
    >>> L = [1, 3, 1]
    >>> replace_items(L, {1: 2, 3: 4, 5: 6})
    >>> L
    [2, 4, 2]
    '''
    
    for i in range(len(L)):
        item = L[i]
        for key in D:
            if item == key:
                L[L.index(item)] = D[key]

def incorrect(L, D):
    # find a test case for which this function fails (3 MARKS)
    ''' (list of int, dict of {int: int}) -> NoneType
    
    >>> L = [1, 1, 2, 2]
    >>> incorrect(L, {1: 2, 2: 4})
    >>> L
    [4, 4, 4, 4]
    >>> L == replace_items(L, {1: 2, 2: 4})
    False
    '''
    for k in D:
        for i in range(len(L)):
            if L[i] == k:
                L[i] = D[k]

if __name__ == '__main__':
    import doctest
    doctest.testmod()