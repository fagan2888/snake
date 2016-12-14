def convert_time_to_seconds(time_as_str):
    ''' (str) -> int
    Precondition: time_as_str is a str in the format 'h:m:s', with
    0 <= int(h) <= 23 and 0 <= int(m) <= 59 and 0 <= int(s) <= 59
    
    Return the number of seconds in time_as_str.
    
    >>> convert_time_to_seconds('1:10:25')
    4225
    '''
    
    time = time_as_str.split(':')
    return 60 * 60 * int(time[0]) + 60 * int(time[1]) + int(time[2])

def number_of_winners(qualifying_time, race_results):
    ''' (str, file open for reading) -> int
    A valid time is a str with format 'h:m:s', with 0 <= int(h) <= 23,
    0 <= int(m) <= 59 and 0 <= int(s) <= 59.
    
    Precondition: qualifying_time is a valid time,
    Each line in race_results contains a single valid time.
    
    Return the number of lines in race_results that contain a time that is
    below qualifying_time.
    '''
    qual_seconds = convert_time_to_seconds(qualifying_time)
    
    count = 0
    for line in race_results:
        line_time = convert_time_to_seconds(line)
        if line_time < qual_seconds:
            count += 1
    return count
