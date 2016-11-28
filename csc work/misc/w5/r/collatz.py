def count_collatz_steps(n):
    ''' (int) -> int
    
    Return the number of steps it takes to reach 1, by repeating the two steps
    of the Collatz conjecture beginning from n.
    
    >>> count_collatz_steps(6)
    8
    '''
    
    count = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
        count = count + 1
    return count
    