def merge_files(file_one, file_two):
    # complete the function body (8 MARKS)
    # you cannot use the list method 'sort'
    ''' (file open for reading, file open for reading) -> list of str
    
    Precondition: both file_one and file_two are in alphabetic order;
    both file_one and file_two contain at least one line; each line
    contains one lowercase word.
    
    Return the combination of the lines from file_one and file_two as a list of
    strings that is in alphabetic order.
    
    >>> file_one = open('file_one.txt')
    >>> file_two = open('file_two.txt')
    >>> merge_files(file_one, file_two)
    ['dryden\n', 'plante\n', 'plante\n', 'potvin\n', 'roy\n', 'sawchuk\n', 'wregget\n']
    '''
    output_list = []
    first_line = file_one.readline()
    second_line = file_two.readline()
    
    while first_line != '' and second_line != '':
        if first_line <= second_line:
            output_list.append(first_line)
            first_line = file_one.readline()
        else:
            output_list.append(second_line)
            second_line = file_two.readline()
    
    if first_line == '':
        output_list.append(second_line)
        final_lines = file_two.readlines()
    else:
        output_list.append(first_line)
        final_lines = file_one.readlines()
    
    output_list.append(final_lines)
    return output_list
