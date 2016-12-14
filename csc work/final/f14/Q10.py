def bubble_sort(L):
    ''' (list) -> NoneType
    Sort the items of L from smallest to largest.
    '''
    
    end = len(L) - 1
    while end != 0:
        # start of a pass of the Bubble Sort algorithm
        for i in range(end): # Line 1
            if L[i] > L[i + 1]: # Line 2
                L[i], L[i + 1] = L[i + 1], L[i] # Line 3
        end = end - 1 # Line 4
    # end of a pass of the Bubble Sort algorithm

# one pass of the algorithm is executed in each iteration of the while loop.
# in the implementation above, a total of len(L) - 1 passes will be executed.
# if the list passed to bubble_sort was almost sorted, it may become sorted
# after a few passes. If the list is sorted at the start of a pass, which
# line of code in the body will not be executed during the pass? (2 MARKS)
# Line 3.

def bubble_sort_revised(L):
    # revise (4 MARKS)
    end = len(L) - 1
    is_sorted = False
    while end != 0 and not is_sorted:
        # start
        is_sorted = True
        for i in range(end):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                is_sorted = False
        end = end - 1

# let n = len(L)
# notice that in the worst case, the runtime grows quadratically wrt n.
# in the best case, n grows quadratically wrt n as well (1 MARK)
# for the revised version, the runtime in the worst case still grows
# quadratically wrt n (1 MARK), but in the best case, the runtime grows
# linearly like n.

# for the following lists:
# L1 = [9, 8, 7, 6, 5, 4, 3, 2, 1] and L2 = [8, 1, 3, 6, 9, 7, 4, 2, 5]
# selection sort will make an equal # of comparisons. (1 MARK)
# insertion sort will make more comparisons with list L1 (1 MARK)
