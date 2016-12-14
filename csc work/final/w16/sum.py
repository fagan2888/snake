def sum_values_above_threshold(value_string, threshold):
    ''' (str, int) -> int
    
    Precondition: value_string.isdigit() returns True
    
    Return the sum of the individual digits in value_string that are 
    greaterthan threshold.
    
    >>> sum_values_above_threshold('153382', 4)
    13
    >>> sum_values_above_threshold('12345', 5)
    0
    '''
    
    sum = 0
    for i in value_string:
        if int(i) > threshold:
            sum += int(i)
    return sum
