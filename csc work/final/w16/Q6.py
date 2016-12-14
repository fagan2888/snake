def read_student_info(filename):
    ''' (str) -> list of object
    
    Return a list representation of the student information stored in the
    file named filename.
    >>> read_student_info('student.txt')
    ['Gries,Paul', ['CSC 108', 'CSC 148', 'CSC 165', 'MAT 137']]
    '''
    
    student_file = open(filename, 'r')
    student_name = read_student_name(student_file)
    course_list = read_student_courses(student_file)
    student_file.close()
    return [student_name, course_list]

def read_student_name(file):
    ''' (file open for reading) -> str
    
    Return a string of the form LAST,FIRST containing the name of the student
    whose information is stored in file.
    '''
    # for line in file:
    #     first_name = file.readline().strip()
    #     last_name = file.readline().strip()
    # return last_name + ',' + first_name
    
    # rewrite the complete body of this buggy function (3 MARKS):
    first_name = file.readline().strip()
    last_name = file.readline().strip()
    return last_name + ',' + first_name

def read_student_courses(file):
    ''' (file open for reading) -> list of str
    
    Return a list containing the courses taken by the student whose information
    is stored in file.
    '''
    
    course_list = []
    for line in file:
        course_list.append(line.strip())
    return course_list

# what is actually returned by the function call: 
# 'read_student_info('student.txt')' if the contents of 'student.txt' is as
# shown in the file.
# ['MAT 137,CSC 165', []] (2 MARKS)
# why? "for line in file:" will execute 6 times. for each time it executes,
# it reads two lines. in the end, first_name and last_name will be set to
# the last two lines respectively.
# the function that has a bug is 'read_student_name'. (1 MARK)