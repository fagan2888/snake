import Q10

class AlarmSchedule:
    ''' contains information about Timestamp objects in an alarm schedule. '''
    
    def __init__(self):
        ''' (AlarmSchedule) -> NoneType
        
        Initialize an AlarmSchedule with an empty list named schedule.
        
        >>> alarms = AlarmSchedule()
        >>> alarms.schedule
        []
        '''
        
        self.schedule = []
    
    def add(self, tstamp):
        ''' (AlarmSchedule, Timestamp) -> NoneType
        
        Modify schedule to add Timestamp tstamp, provided there is not an
        existing Timestamp with the same time.
        
        >>> alarms = AlarmSchedule()
        >>> alarms.add(Timestamp(14, 10, 42, 'Relax'))
        >>> alarms.add(Timestamp(14, 23, 39, 'Sigh'))
        >>> alarms.add(Timestamp(14, 10, 42, 'Burp'))
        >>> alarms.schedule[0].msg
        'Relax'
        >>> alarms.schedule[1].msg
        'Sigh'
        >>> len(alarms.schedule)
        2
        '''
        boolean = True
        for i in range(len(self.schedule)):
            if self.schedule[i].time() == tstamp.time():
                boolean = False
        
        if boolean == True:
            self.schedule.append([tstamp.time(), tstamp.msg])