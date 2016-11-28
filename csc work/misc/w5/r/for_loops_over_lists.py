def collect_underperformers(num, threshold):
    ''' (list of number, int) -> list of number
    
    Return a new list consisting of those numbers in num that are 
    below threshold, in the same order as in nums.
    
    >>> collect_underperformers([1, 2, 3, 4], 3)
    [1, 2]
    >>> collect_underperformers([1, 2, 108, 3, 4], 50)
    [1, 2, 3, 4]
    >>> collect_underperformers([], 7)
    []
    '''
    
    underperformers = []
    for i in range(len(num)):
        if num[i] < threshold:
            underperformers.append(num[i])
    return underperformers
    
def scale_midterm_grades(grades, multiplier, bonus):
    ''' (list of number, number, number) -> NoneType

    Modify each grade in grades by multiplying it by multiplier and then
    adding bonus. Cap grades at 100.

    >>> grades = [45, 50, 55, 95]
    >>> scale_midterm_grades(grades, 1, 10)
    >>> grades
    [55, 60, 65, 100]
    '''
    
    for i in range(len(grades)):
        grades[i] = min((grades[i] * multiplier) + bonus, 100)
