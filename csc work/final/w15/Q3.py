def cut_in_half(message):
    # include three more test cases (3 MARKS)
    ''' (str) -> list of str
    Return a two-item list in which the first item is the first half of message
    and the second item is the second half of message. If the two halves of
    message are not the same length, the longer half should appear as the first
    item in the list.
    Case #1: empty string
    Case #2: one character string
    Case #3: multi-character string, odd length
    Case #4: multi-character string, even length
    Case #5: two-character string, first character is a space.
    
    >>> cut_in_half('')
    ['', '']
    >>> cut_in_half('p')
    ['p', '']
    >>> cut_in_half('aaaaa')
    ['aaa', 'aa']
    >>> cut_in_half('abcabc')
    ['abc', 'abc']
    >>> cut_in_half(' a')
    ['', 'a']
    '''
    length = len(message)
    m1 = message[:length//2 + 1]
    m2 = message[length//2 + 1:]
    return [m1, m2]
    
def convocation_status(gpa):
    # include four more test cases (3 MARKS)
    ''' (float) -> str
    Precondition: 0.0 <= gpa <= 4.0
    Return 'with high distinction' if gpa is at least 3.5, 'with distiction' if
    gpa is at least 3.2 and less than 3.5, and 'regular' otherwise.
    Case #1: under 3.2
    Case #2: exactly between 3.2 and 3.5
    Case #3: above 3.5
    Case #4: exactly 3.5
    Case #5: exactly 3.2
    
    >>> convocation_status(3.1)
    'regular'
    >>> convocation_status(3.3)
    'with distinction'
    >>> convocation_status(4.0)
    'with high distinction'
    >>> convocation_status(3.5)
    'with high distinction'
    >>> convocation_status(3.2)
    'with distinction'
    '''
    
    status = 'regular'
    if gpa >= 3.5:
        status = 'with high distinction'
    elif 3.2 <= gpa < 3.5:
        status = 'with distinction'
    return status

if __name__ == '__main__':
    import doctest
    doctest.testmod()