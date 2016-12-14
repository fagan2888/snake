def remove_unnecessary_spaces(message):
    ''' (str) -> str
    
    Precondition: message contains at least one non-space character
    
    Return message with any occurences of more than one consecutive space
    removed, and any spaces at the start or end removed.
    >>> remove_unnecessary_spaces(' I like Python.  Welcome to  108!   ')
    'I like Python. Welcome to 108!'
    >>> remove_unnecessary_spaces('Hello,             can you hear me?')
    'Hello, can you hear me?'
    '''
    
    SPACE = ' '
    message = message.strip()
    
    new_message = message[0]
    
    for ch in message[1:]:
        if ch != SPACE or new_message[-1] != SPACE:
            new_message += ch
    return new_message

