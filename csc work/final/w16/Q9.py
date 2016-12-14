def loyalty_status(points):
    # Write four additional test cases (4 MARKS)
    ''' (int) -> str
    
    Precondition: points >= 0
    
    Return 'Elite' if points is 2500 or more, 'Regular' if points is 1000 or
    more but less than 2500, and 'New' otherwise.
    
    Test cases:
    Case #1: over 2500
    Case #2: under 2500, over 1000
    Case #3: under 1000
    Case #4: equals 1000
    Case #5: equals 2500
    >>> loyalty_status(2501)
    'Elite'
    >>> loyalty_status(1500)
    'Regular'
    >>> loyalty_status(900)
    'New'
    >>> loyalty_status(1000)
    'Regular'
    >>> loyalty_status(2500)
    'Elite'
    '''
    if points >= 2500:
        return 'Elite'
    elif (1000 <= points < 2500):
        return 'Regular'
    else:
        return 'New'
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
# part b: (2 MARKS)
# fill in the box
# status = 'New'
# if (points >= 2500):
#     status = 'Elite'
# if (1000 <= points < 2500):
#     status = 'Regular'
# return status