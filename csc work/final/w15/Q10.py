class Timestamp:
    ''' Time and message for a timestamp. '''
    
    def __init__(self, h, m, s, msg):
    ''' (Timestamp, int, int, int, str) -> NoneType
    
    Precondition: 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59
    Initialize the hour h, minute m, second s, and message msg associated
    with this Timestamp.
    
    >>> ts1 = Timestamp(14, 10, 42, 'Relax')
    >>> ts1.hour
    14
    >>> ts1.min
    10
    >>> ts1.sec
    42
    >>> ts1.msg
    'Relax'
    '''
    self.hour = h
    self.min = m
    self.sec = s
    self.msg = msg
    
    def time(self):
        ''' (Timestamp) -> str
        
        Return a string representation of the time associated with this
        Timestamp.
        
        >>> ts1 = Timestamp(14, 9, 1, 'Relax')
        >>> ts1.time()
        '14:9:1'
        '''
        
        return str(self.hour) + ':' + str(self.min) + ':' + str(self.sec)
    
    def __eq__(self, other):
        ''' (Timestamp, Timestamp) -> bool
        
        Returns a boolean indicating whether or not a Timestamp contains the
        same information as another Timestamp. The two are considered equal if
        they have the same time (hour, minute and second) and the same message.
        '''
        
        return (self.time() == other.time() and self.msg == other.msg)
