# complete the body of the function (7 MARKS)

def numeric_phone(alphanumeric_phone, mapping):
    ''' (str, list of str) -> int
    
    Preconditions:
    - len(mapping) <= 10
    - alphanumeric_phone contains only digits and uppercase letters
    - each letter in alphanumeric_phone is guaranteed to appear in mapping once
    - mapping may contain letters not in alphanumeric_phone
    
    Return a numeric phone number that corresponds to alphanumeric_phone.
    Each letter from alphanumeric_phone is replaced with the index of the item 
    from mapping that contains the letter. Digits are not replaced.
    
    >>> numeric_phone('416310BELL', ['ABC', 'DEF', 'GHI', 'JKL', 'NO', 'PQRS', 'TUV', 'WXYZ'])
    4163100133
    '''
    
    new_number = ''
    for char in alphanumeric_phone:
        if char.isalpha():
            for i in range(len(mapping)):
                if char in mapping[i]:
                    char = str(i)
        new_number += char
    return int(new_number)
