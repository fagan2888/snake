def is_palindrome(string):
    """ (str) -> bool
    
    Return True if and only if string is a palindrome.
    Precondition: string is all in lowercase.
    
    >>>> is_palindrome('ABCDEFG')
    ''
    >>>> is_palindrome('madamimadam')
    True
    >>>> is_palindrome('Racecar')
    ''
    >>>> is_palindrome('racecars')
    False
    """
    
    if string.islower():
        return string == string[::-1]
    else:
        return ''
        
def is_palindromic_phrase(phrase):
    """ (str) -> bool
    
    Return True if and only if the string phrase is a palindrome,
    ignoring both case (considering uppercase equivalent to their lowercase
    form) and non-alphabetic characters (ignoring these completely).
    
    >>>> is_palindromic_phrase('Madam, I'm Adam')
    True
    >>>> is_palindromic_phrase('A man, a plan, a canal, Panama.')
    True
    >>>> is_palindromic_phrase('The rain in spain falls mainly on the plane')
    False
    """
    
    phrase = phrase.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_phrase = ''
    for char in phrase:
        if char in alphabet:
            new_phrase += char
            
    return is_palindrome(new_phrase)
        
def get_odd_palindrome_at(string, index):
    """ (str, int) -> str
    
    Returns the longest odd-length palindrome in the string which is centred
    at the specified index.
    Preconditions: 0 <= index <= len(string), string is all in lowercase.
    
    >>>> get_odd_palindrome_at('abcdefedcba', 5)
    'abcdefedcba'
    >>>> get_odd_palindrome_at('abcdefedcbafgsfds', 5)
    'abcdefedcba'
    >>>> get_odd_palindrome_at('fgsfdsabcdefedcba', 11)
    'abcdefedcba'
    >>>> get_odd_palindrome_at('ABCDEFEDCBA', 5)
    ''
    """
    
    if string.islower():
        palindrome = ''
        distance_from_end = len(string) - index
        if distance_from_end < index:
            count = distance_from_end
        else:
            count = index
        for spot in range(1, count + 1):
            candidate = (string[index - spot: index + spot + 1])
            if is_palindrome(candidate) and len(candidate) > len(palindrome):
                palindrome = candidate
        return palindrome
    else:
        return ''