def first_function(values):
    ''' (list of int) -> NoneType
    '''
    
    for i in range(len(values)):
        if values[i] % 2 == 1:
            values[i] += 1

def second_function(value):
    ''' (int) -> int
    '''
    
    if value % 2 == 1:
        value += 1
    return value

def snippet_1():
    a = [1, 2, 3]
    b = 1
    first_function(a)
    second_function(b)
    print(a)
    print(b)
    
    # output: (2 MARKS)
    # [2, 2, 4]
    # 1
    # why? second_function(1) will not return 2 if we don't print it.
    
def snippet_2():
    a = [1, 2, 3]
    b = 1
    print(first_function(a))
    print(second_function(b))
    
    # output: (2 MARKS)
    # None
    # 2
