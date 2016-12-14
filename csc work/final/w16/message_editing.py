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

def shorten_messages(message_list):
    ''' (list of str) -> NoneType
    Modify message_list so that any occurences of consecutive spaces in each
    message, as well as any unnecessary spaces at the start and end of each 
    message, are removed.
    
    >>> message_list = ['Hi         there   !!  ', ' CSC    108']
    >>> shorten_messages(message_list)
    >>> message_list
    ['Hi there !!', 'CSC 108']
    '''
    
    for i in range(len(message_list)):
        message_list[i] = remove_unnecessary_spaces(message_list[i])
        # remove_unecessary_spaces is called k-many times, for k the length
        # of message_list. this executes in linear time.