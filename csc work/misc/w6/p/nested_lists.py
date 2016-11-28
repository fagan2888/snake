def calculate_average(asn_grades):
    ''' (list of list of [str, number]) -> float
    
    Return the average of the grades in asn_grades.
    
    >>> calculate_average([['A1', 80], ['A2', 90]])
    85.0
    '''
    
    total = 0
    for i in range(len(asn_grades)):
        total += asn_grades[i][1]
    return total / len(asn_grades)
    