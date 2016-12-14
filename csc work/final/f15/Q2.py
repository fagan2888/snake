def top_three(scores):
    # complete the function body (5 MARKS)
    # must use the following algorithm:
    # 1. create a copy of the original list
    # 2. create a new empty list to hold the biggest three numbers
    # 3. find the biggest number in the copy of the original list, add it
    # to the new list, and remove it from a copy of the original list.
    # repeat twice.
    
    ''' (list of int) -> list of int
    
    Precondition: len(scores) >= 3
    
    Return a new list that contains the three largest numbers from scores.
    >>> top_three([5, 4, 6, 3, 1, 2, 7])
    [7, 6, 5]
    >>> top_three([6, 2, 11, 12, 7, 12, -3])
    [12, 12, 11]
    '''
    
    list_copy = scores[:]
    biggest_three = []
    for i in range(3):
        biggest = max(list_copy)
        biggest_three.append(biggest)
        list_copy.remove(biggest)
    return biggest_three
    
def top_three_mutate(scores):
    # complete the function body (5 MARKS)
    # must use the following algorithm:
    # remove the smallest number from the list repeatedly until only
    # the three largest numbers remain in the list
    '''(list of int) -> NoneType
    Precondition: len(scores) >= 3
    
    Modify scores so that it contains only the three largest numbers,
    in the same order they appear in the original list.
    
    >>> my_scores = [5, 4, 6, 3, 1, 2, 7]
    >>> top_three_mutate(my_scores)
    >>> my_scores
    [5, 6, 7]
    >>> my_scores = [6, 2, 12, 11, 7, 12, -3]
    >>> top_three_mutate(my_scores)
    >>> my_scores
    [12, 11, 12]
    '''
    
    while len(scores) != 3:
        scores.remove(min(scores))