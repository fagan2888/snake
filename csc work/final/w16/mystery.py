def mystery(s1, s2, s3):
    ''' (str, str, str) -> int
    
    Precondition: len(s1) == len(s2) == len(s3)
    
    Return the number of characters with matching positions between the
    three strings.
    >>> mystery('cat', 'bat', 'hat')
    2
    >>> mystery('cat', 'dog', 'log')
    0
    '''
    
    count = 0
    for i in range(len(s1)):
        if s1[i] == s2[i] and s2[i] == s3[i]:
            count = count + 1
    return count

# the maximum number of times the line 'count = count + 1' could be executed:
# (in terms of k): k
# if k = 3, then 'count = count + 1' is executed at a maximum 3 times with the
# argument: mystery('aaa', 'aaa', 'aaa')
# the minimum number of times the line 'count = count + 1' could be executed:
# (in terms of k): 0 * k