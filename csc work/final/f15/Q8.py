import random

def bogosort(lst):
    ''' (list of int) -> NoneType
    
    Modify lst to sort the items from smallest to largest.
    
    >>> my_list = [42, 17, 56]
    >>> bogosort(my_list)
    >>> my_list
    [17, 42, 56]
    '''
    while not is_sorted_list(lst):
        random.shuffle(lst)

def is_sorted_list(lst):
    # complete the body of the function (4 MARKS)
    ''' (list of int) -> bool
    
    Return True if and only if the items in lst are sorted from smallest
    to largest.
    
    >>> is_sorted_list([12, 12, 2015])
    True
    >>> is_sorted_list([11, 1, 2016])
    False
    '''
    
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
    
    # best case running time: i.e. when is_sorted_list performs the fewest
    # possible # of comparisons.
    # a list of length 4 with the best case running time (1 MARK):
    # [2, 1, 3, 4]
    # best case running time (1 MARK): constant
    # a list of length 4 with the worst case running time (1 MARK):
    # [1, 2, 3, 4]
    # worst case running time (1 MARK): linear

if __name__ == '__main__':
    import doctest
    doctest.testmod()