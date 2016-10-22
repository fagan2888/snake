import math

def distance(x, y):
    """ (number, number) -> float
    
    Return distance of a point with coordinates x
    and y from the origin.
    
    >>> distace(3, 4)
    5.0
    """
    
    # formula: d = sqrt((x ** 2) + (y **2))
    return math.sqrt((x ** 2) + (y **2))

# Part 2
# Function Design Recipe
# Examples, Type Contract, Header, Description, Code, Test (ETHDCT)

def repeat_word(word, num_repeats):
    """ (str, int) -> str
    
    Return word repeated num_repeats times.
    
    >>> repeat_word('Marcia ', 3)
    'Marcia Marcia Marcia'
    >>> repeat_word('Hi', 0)
    ''
    
    """
    
    return word * num_repeats

def number_of_cents(change):
    """ (float) -> int

    Returns the number of cents in change after all
    of the whole numbers have been removed.
    
    >>> number_of_cents(1.25)
    25 
    >>> number_of_cents(20.00)
    0
    """

    dollar_remainder = change % 1
    cents = dollar_remainder * 100
    return round(cents)

def calculate_tax(bill, taxrate):
    """ (number, number) -> number
    
    Return the amount of tax to be paid on bill
    when the tax rate is taxrate.
    
    >>> calculate_tax(100, 0.23)
    23.0
    >>> calculate_tax(5, 0)
    0
    """
    
    return bill * taxrate