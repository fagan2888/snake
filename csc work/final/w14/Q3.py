def return_mix(num, word):
    ''' (int, str) -> object
    
    Precondition: word contains at least 3 characters.
    '''
    
    if word[2] == 'r':
        return 2 * num
    elif num > 10:
        return (word + word)
    elif word[1:3] == 'ab':
        return (2 == 3)
    
    # function call: return_mix(5, 'Canada')
    # return value: None
    # return type: NoneType
    
    # function call: return_mix(12, 'Toronto')
    # return value: 24
    # return type: int
    
    # function call: return_mix(16, 'Canada')
    # return value: 'CanadaCanada'
    # return type: str
    
    # function call: return_mix(-2, 'cabinet')
    # return value: False
    # return type: boolean
    
    # function call: return_mix(11, return_mix(11, 'Can'))
    # return value: 'CanCanCanCan'
    # return type: str