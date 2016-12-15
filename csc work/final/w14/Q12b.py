class Flight:
    ''' Information about an airplane flight. '''
    
    def __init__(self, plane):
        ''' (Flight, Airplane) -> NoneType
        Create a Flight with an empty passenger list on airplane plane.
        >>> a = Airplane('Boeing 747', '19643', 366, 45267.7)
        >>> f = Flight(a)
        >>> str(f.airplane)
        'Airplane(Boeing 747, 19643, 366, 45267.7)'
        >>> f.passengers
        []
        '''
        
        self.airplane = plane
        self.passengers = []
    
    def add(self, passenger):
        ''' (Flight, str) -> bool
        
        If there are still seats available on this flight, add passenger to
        the passenger list. Retrn True iff the passenger is added to
        this flight.
        
        >>> a = Airplane('Cessna 150E', '9378', 1, 824.8)
        >>> f = Flight(a)
        >>> f.add('Myrto')
        True
        >>> f.add('Jen')
        False
        '''
        if len(self.passengers) < self.airplane.seats:
            self.passengers.append(passenger)
            return True
        return False
    
    def change_planes(self, other_airplane):
        ''' (Flight, Airplane) -> bool
        
        If other_airplane has enough seats to hold the passengers on this 
        flight, use other_airplane for this flight. Whether or not we change 
        to other_airplane, return the number of available seats on this flight 
        (seats not currently occupied by passengers).
        
        >>> a1 = Airplane('Boeing 747', '19643', 366, 45267.7)
        >>> f = Flight(a1)
        >>> f.add('Myrto')
        True
        >>> f.add('Jen')
        True
        >>> a2 = Airplane('Bombardier Dash 8', '11234', 39, 6444.6)
        >>> f.change_planes(a2)
        37
        >>> a3 = Airplane('Cessna 150E', '9378', 1, 824.8)
        >>> f.change_planes(a3)
        37
        '''
        
        num_seats = self.airplane.seats
        num_passengers = len(self.passengers)
        if num_passengers <= other_airplane.seats:
            self.airplane = other_airplane
        return num_seats - num_passengers
