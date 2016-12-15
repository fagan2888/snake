def c_1():
    ['Hello', 'there!'].split()
    # error: list has no method split
    
def c_2():
    'April' + 16
    # error: cannot concatenate str and int
    
def c_3():
    ['Temperature', 'is'].extend(10)
    # error: int is not iterable, cannot apply extend with argument of type int.
    
def c_4():
    degrees_to_season = {[25]: 'summer', [-15]: 'winter'}
    # error: need to use immutable types for dictionary keys. lists are mutable.
    
def c_5():
    word = 'computer'
    word[8]
    # error: len(word) < 8, so word[8] doesn't point anywhere.
