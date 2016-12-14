VOWELS = 'aeiou'

def separate_message(message):
    # write three more test cases (3 MARKS)
    ''' (str) -> list of str
    Precondition: message.isalpha() and message.islower()
    
    Return a two-item list in which the first item is a str that contains the 
    different vowels that occur in message, in the same order as they first 
    appear in message, and the second item is a str that contains the different 
    consonants (non-vowels) that occur in message, in the same order as they 
    first appear in message.
    
    Case #1: multi-character string, repeated vowels and consonants
    Case #2: multi-character string, only vowels, includes repeats
    Case #3: multi-character string, only consonants, includes repeats
    Case #4: empty string
    >>> separate_message('papadopoulou')
    ['aou', 'pdl']
    >>> separate_message('aeioaeioaaeiu')
    ['aeiou', '']
    >>> separate_message('bcdfghbdfhgxzqrs')
    ['', 'bcdfghxzqrs']
    >>> separate_message('')
    ['', '']
    '''
    
    list = []
    string_vowels = ''
    string_consonants = ''
    for char in message:
        if char in VOWELS and char not in string_vowels:
            string_vowels += char
        elif char not in VOWELS and char not in string_consonants:
            string_consonants += char
    list.append(string_vowels)
    list.append(string_consonants)
    return list
    
def frequent_flyer_status(miles):
    # write four more test cases (4 MARKS)
    ''' (int) -> str
    
    Precondition: miles >= 0
    
    Return 'Gold' if miles is at least 1000, 'Silver' if miles is at least 500
    and less than 1000, and 'Bronze' otherwise.
    
    Case #1: under 500
    Case #2: over 1000
    Case #3: strictly between 500 and 1000
    Case #4: exactly 500
    >>> frequent_flyer_status(499)
    'Bronze'
    >>> frequent_flyer_status(1001)
    'Gold'
    >>> frequent_flyer_status(750)
    'Silver'
    >>> frequent_flyer_status(500)
    'Silver'
    '''
    output = 'Bronze'
    if miles >= 1000:
        output = 'Gold'
    if 500 <= miles < 1000:
        output = 'Silver'
    return output

if __name__ == '__main__':
    import doctest
    doctest.testmod()