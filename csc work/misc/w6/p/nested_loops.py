def averages(grades):
    ''' (list of list of number) -> list of float
    
    Return a new list in which each item is the average of the grades in
    the inner list at the corresponding position of grades.
    
    >>> averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    '''
    
    #averages = []
    #for i in range(len(grades)):
    #    total = 0
    #    for j in range(len(grades[i])):
    #        total += grades[i][j]
    #    average = total / len(grades[i])
    #    averages.append(average)
    #return averages
    
    averages = []
    for grades_list in grades:
        total = 0
        for mark in grades_list:
            total += mark
        averages.append(total / len(grades_list))
    return averages