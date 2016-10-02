def factorial(n):
    ''' (int) -> int
    
    Returns n! for any positive integer n.
    
    >>> 0!
    1
    >>> 2!
    2
    >>> 3!
    6
    '''
    k = 1
    for i in range(n):
        k *= (i + 1)
    return k

factorial(10)
