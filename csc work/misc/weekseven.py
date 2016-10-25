def write_to_file(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Precondition: the strings in sentences contain no newlines

    Write each sentence from sentences to file, one per line.
    """

    for s in sentences:
            file.write(s)
            file.write('\n')

def increment_values(d):
    """ (dict with number values) -> NoneType

    Increase each value in d by 1.
    """
    for k in d:
        d[k] = d[k] + 1

def contains(value, lst):
    """ (object, list of list of object) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
    True
    """

    found = False  # We have not yet found value in the list.

    for i in range(len(lst)):
            for j in range(len(lst[i])):
                if lst[i][j] == value:
                    found = True
    #for sublist in lst:
     #       if value in sublist:
      #          found = True

    return found