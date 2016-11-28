def reverse(s):
    ''' (str) -> str
    
    Return a reversed version of s.
    
    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    '''
    new = ''
    for i in range(len(s)):
        new += s[len(s) - 1 - i]
    return new
    

def is_palindrome(s):
    ''' (str) -> bool
    
    Return True iff s is a palindrome.
    
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    '''
    
    return reverse(s) == s
    
def is_palindrome2(s):
    ''' (str) -> bool
    
    Return True iff s is a palindrome.
    
    >>> is_palindrome2('noon')
    True
    >>> is_palindrome2('racecar')
    True
    >>> is_palindrome2('dented')
    False
    '''
    
    half_s = ''
    if (len(s) % 2) == 0:
        half_s += s[len(s) // 2 :]
    else:
        half_s += s[(len(s) // 2) + 1:]
    return reverse(half_s) == s[:len(s) // 2]
    
    # compare the first half of s to the reverse of the second half
    # omit the middle character of an odd-length string
    #n = len(s)
    #return s[:n // 2] == reverse(s[n - n // 2:])
    
def is_palindrome3(s):
    
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True
    
    #i = 0
    #j = len(s) - 1
    #while i < j and s[i] == s[j]:
    #   i += 1
    #   j -= 1
    #return j <= i