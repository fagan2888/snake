def change_password(files_list, new_password):
    # debug the body of the function (4 MARKS)
    # there are four bugs.
    ''' (list of str, str) -> str
    Preconditions:
    (1) files_list is not empty.
    (2) Each file in files_list contains one single-line password.
    (3) All files in files_list contain passwords of different lengths.
    (4) Your 6-character password is guaranteed to be in one of these files.
    
    In the appropriate file from files_list, replace your 6-character password
    with new_password, and return your old password.
    '''
    found = False    # from True to False
    for filename in files_list:    # from [:-1] to ''
        passwd_file = open(filename, 'r')
        first_line = passwd_file.readline() #from read() to readline()
        password = first_line.strip()    # from strip('2') to strip()
        if len(password) == 6:   #from password to len(password)
            passwd_file.close()
            passwd_file = open(filename, 'w')
            passwd_file.write(new_password)
            found = True
        passwd_file.close()
        if found:   # this is correct, do not modify
            return password