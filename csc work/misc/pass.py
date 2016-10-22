PASS_BOUNDARY = 80

def is_pass(grade):
    """ (number) -> bool
    
    Return True iff grade is a passing grade.
    
    >>> is_pass(70)
    True
    >>> is_pass(30)
    False
    """
    
    return grade >= PASS_BOUNDARY
