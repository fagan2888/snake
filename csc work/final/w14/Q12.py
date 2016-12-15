class Airplane:
    ''' Information about a particular airplane including the model, the serial
    number, the number of seats, and the number of miles travelled.
    '''
    
    def __init__(self, plane_model, serial_num, num_seats, miles_travelled):
        ''' (Airplane, str, str, int, float)
        Record the airplane's model plane_model, serial number serial_num, the
        number of seats, and the distance travelled miles_travelled.
        >>> airplane = Airplane('Boeing 747', '19643', 366, 45267.7)
        >>> airplane.model
        'Boeing 747'
        >>> airplane.serial
        '19643'
        >>> airplane.seats
        366
        >>> airplane.miles
        45267.7
        '''
        
        self.model = plane_model
        self.serial = serial_num
        self.seats = num_seats
        self.miles = miles_travelled
    
    def log_trip(self, num_miles):
        ''' (Airplane, float) -> NoneType
        
        Precondition: num_miles > 0.0
        
        Record that the airplane travelled num_miles additional miles
        '''
        
        self.miles += num_miles
    
    def __eq__(self, other):
        ''' (Airplane, Airplane) -> bool
        
        Compares two Airplane objects and returns a boolean indicating if they
        are equal. Two Airplanes are equal if they have the same serial number.
        '''
        
        return self.serial == other.serial