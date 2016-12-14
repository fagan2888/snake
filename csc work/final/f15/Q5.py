CURRENT_YEAR = 2015

def get_age(birthday_string):
    # complete the body of the function (3 MARKS)
    # 'end of current year' = 2015-12-31
    ''' (str) -> int
    
    Precondition: birthday_string has format YYYY-MM-DD and represents a valid
    year, month, and day, no later than the end of CURRENT_YEAR.
    
    Return the age of the person with the birthdate birthday_string at the end
    of the year CURRENT_YEAR.
    
    >>> get_age('2006-08-08')
    9
    >>> get_age('1997-12-31')
    18
    >>> get_age('2015-01-01')
    0
    '''
    birthday_data = birthday_string.split('-')
    return CURRENT_YEAR - int(birthday_data[0])
    
    def write_age_file(data_file, age_file):
        ''' (file open for reading, file open for writing) -> NoneType
        
        Precondition: data_file is a valid Skype data file.
        
        Write the age of each user in the data_file to its own line in age_file.
        The age of a user is as defined in Part (a).
        '''
        for line in data_file:
            if line.strip == 'BIRTHDATE':
                birthday = data_file.readline().strip()
                age_file.write(str(get_age(birthday)) + '\n')
                
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()