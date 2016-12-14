def cocktailsort(lst):
    ''' (list of number) -> NoneType
    
    Modify lst to sort the items for smallest to largest.
    
    >>> my_list = [4, 2, 5, 8, 6, 7, 3, 1]
    >>> cocktailsort(my_list)
    >>> my_list
    [1, 2, 3, 4, 5, 6, 7, 8]
    '''
    
    top = len(lst) - 1
    bottom = 0
    
    while top > bottom:
        sort_to_top(lst, bottom, top)
        top = top - 1
        sort_to_bottom(lst, bottom, top)
        bottom += 1

def sort_to_top(lst, bottom, top):
    ''' (list of number, int, int) -> NoneType
    
    Modify lst to swap the largest item in lst[bottom: top + 1] to index top.
    
    >>> my_list = [1, 2, 4, 6, 3, 5, 7, 8]
    >>> sort_to_top(my_list, 2, 5)
    >>> my_list
    [1, 2, 4, 5, 3, 6, 7, 8]
    '''
    
    index_of_largest = bottom
    
    for j in range(bottom + 1, top + 1):
        if lst[j] > lst[index_of_largest]:
            index_of_largest = j
    
    lst[index_of_largest], lst[top] = lst[top], lst[index_of_largest]
    
def sort_to_bottom(lst, bottom. top):
    ''' (list of number, int, int) -> NoneType
    
    Modify lst to swap the smallest item in lst[bottom: top + 1] to index
    bottom.
    
    >>> my_list = [1, 2, 4, 5, 3, 5, 7, 8]
    >>> sort_to_bottom(my_list, 2, 4)
    >>> my_list
    [1, 2, 3, 5, 4, 6, 7, 8]
    '''
    
    # complete the function body (4 MARKS)
    index_of_smallest = bottom
    
    for j in range(bottom + 1, top + 1):
        if lst[j] < lst[index_of_smallest]:
            index_of_smallest = j
        
    lst[index_of_smallest], lst[bottom] = lst[bottom], lst[index_of_smallest]
    
    # examine the runtime behavior (1 MARK):
    # 'This algorithm does not have a different best and worst case number
    # of comparisons'