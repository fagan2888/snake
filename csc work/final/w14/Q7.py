def count_letter_case(L):
    # complete the function body (6 MARKS)
    ''' (list of list of str) -> list of tuple of int
    
    Precondition: each str in L is non-empty and contains only alphabetic 
    characters
    
    Count the number of words in each sublist of L that start with lowercase 
    and uppercase letters. Return a new list where each element is a two-item 
    tuple in which the first item is the number of words in the list at the 
    corresponding index of L that start with a lowercase letter and the second 
    item is the number of words in the list at the corresponding index of L 
    that start with an uppercase letter.
    
    >>> count_letter_case([['apple', 'Banana'], ['PEAR'], [], ['PEACH', 'apRICot', 'plum']])
    [(1, 1), (0, 1), (0, 0), (2, 1)]
    '''
    
    letter_cases = []
    for i in range(len(L)):
        sublist = L[i]
        num_lowercase = 0
        num_uppercase = 0
        for j in range(len(sublist)):
            if sublist[j][:1].isupper():
                num_uppercase += 1
            else:
                num_lowercase += 1
        letter_cases.append((num_lowercase, num_uppercase))
    return letter_cases
    
def count_letter_case_mutate(L):
    # complete the function body (3 MARKS)
    ''' (list of list of str) -> NoneType
    Precondition: each str in L is non-empty and contains only alphabetic 
    characters
    
    Replace each item in L with a two-item tuple in which the first item is
    the number of words in the list at the corresponding index of L that start 
    with a lowercase letter and the second item is the number of words in the 
    list at the corresponding index of L that start with an uppercase letter
    
    >>> data = [['apple', 'Banana'], ['PeAr'], [], ['PEACH', 'apRICot', 'plum']]
    >>> count_letter_case_mutate(data)
    >>> data
    [(1, 1), (0, 1), (0, 0), (2, 1)]
    '''
    
    for i in range(len(L)):
        sublist = L[i]
        num_lowercase = 0
        num_uppercase = 0
        for j in range(len(sublist)):
            if sublist[j][:1].isupper():
                num_uppercase += 1
            else:
                num_lowercase += 1
        L[i] = ((num_lowercase, num_uppercase))

def helper(L):
    # write a possible helper function (2 MARKS)
    num_lowercase = 0
    num_uppercase = 0
    for i in range(len(L)):
        if L[:1].isupper():
            num_uppercase += 1
        else:
            num_lowercase += 1
    return ((num_lowercase, num_uppercase))
