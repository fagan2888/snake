SPECIAL_CASE_SCHOOL_1 = 'Fort McMurray Composite High'
SPECIAL_CASE_SCHOOL_2 = 'Father Mercredi High School'
SPECIAL_CASE_YEAR = '2016'
NO_EXAM = 'NE'
ADMISSION_ACCEPTED = 'accept'
ADMISSION_SCHOLARSHIP = 'accept with scholarship'
ADMISSION_REJECTED = 'reject'


def is_special_case(record):
    """ (str) -> bool

    Return True iff the student represented by record is a special case.

    >>> is_special_case('Jacqueline Smith,Fort McMurray Composite High,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    True
    >>> is_special_case('Jacqueline Smith,Father Something High School,2016,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    False
    >>> is_special_case('Jacqueline Smith,Fort McMurray Composite High,2015,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    False
    """
    
    return ((SPECIAL_CASE_SCHOOL_1 or SPECIAL_CASE_SCHOOL_2) in record) and (SPECIAL_CASE_YEAR in record)


def get_final_mark(record, course_mark, exam_mark):
    """ (str, str, str) -> float
    
    Return the student's final mark from a particular course obtained from 
    their record computed as the average of their course mark and exam mark. 
    If the student's record indicates that they are a special case and they did 
    not write a final exam then their final mark is set as their course mark.
    
    >>> get_final_mark('Paul Gries,Ithaca High School,1986,BIO,60,70,CHM,80,90,CAT,10,20,BEng', '10', '20')
    15.0
    >>> get_final_mark('Paul Gries,Ithaca High School,1986,BIO,60,70,CHM,80,90,CAT,10,20,BEng', '80', '90')
    85.0
    >>> get_final_mark('Jacqueline Smith,Fort McMurray Composite High,2016,MAT,90,NE,ENG,92,88,CHM,80,85,BArts', '90', 'NE')
    90.0
    >>> get_final_mark('Paul Gries,Ithaca High School,1986,BIO,60,70,CHM,80,NE,CAT,10,20,BEng', '80', 'NE')
    40.0
    """
    
    if course_mark.isdigit() and exam_mark.isdigit():
        return (float(course_mark) + float(exam_mark)) / 2
    elif exam_mark == NO_EXAM:
        if is_special_case(record):
            return float(course_mark)
        else:
            return float(course_mark) / 2
    else:
        return 0.0


def get_both_marks(record, course_code):
    """ (str, str) -> str
    
    Return a string containing the course mark and final mark respectively, 
    separated by a single space, corresponding to a particular course code 
    from the record. If the course code is absent from the record
    then return an empty string.
    
    >>> get_both_marks('Jacqueline Smith,Fort McMurray Composite High,2015,MAT,90,94,ENG,92,88,CHM,80,85,BArts', 'MAT')
    '90 94'
    >>> get_both_marks('Jacqueline Smith,Fort McMurray Composite High,2015,MAT,90,94,ENG,92,88,CHM,80,85,BArts', 'CAT')
    ''
    >>> get_both_marks('Paul Gries,Ithaca High School,1986,BIO,60,70,CHM,80,NE,CAT,10,20,BEng', 'CHM')
    '80 NE'
    """
    
    if course_code in record:
        i = record.index(course_code)
        return record[(i + 4):(i + 6)] + " " + record[(i + 7):(i + 9)]
    else:
        return ''


def extract_course(transcript, course):
    """ (str, int) -> str
    
    Return a string containing a course code, course mark and final mark, 
    in that order. The second argument specifies the order in which the course
    appears in the transcript.
    
    >>> extract_course('MAT,90,94,ENG,92,NE,CHM,80,85', 2)
    'ENG,92,NE'
    >>> extract_course('MAT,90,94,ENG,92,NE,CHM,80,85', 4)
    ''
    """
    
    if 1 <= course < 4:
        index = 0;
        if course == 2:
            index = 10;
        elif course == 3:
            index = 20
        return transcript[index: index + 9]
    else:
        return ''
    

def applied_to_degree(record, degree):
    """ (str, str) -> bool
    
    Return True iff the student represented by record has applied to the
    specified degree program.
    
    >>> applied_to_degree('Paul Gries,Ithaca High School,1986,BIO,60,70,CHM,80,90,CAT,95,96,BEng', 'BEng')
    True
    >>> applied_to_degree('Jacqueline Smith,Fort McMurray Composite High,2015,MAT,90,NE,ENG,92,88,CHM,80,85,BArts', 'BEng')
    False
    """
    
    return degree in record
    

def decide_admission(average, cutoff):
    """ (number, number) -> str
    
    Return a string describing whether a student has been accepted, rejected, 
    or accepted with scholarship to a program based on the average of accepted 
    courses for admission and the cutoff threshold mark. If the average is five
    points higher than the necessary cutoff, then the student is accepted with
    scholarship.
    
    >>> decide_admission(18, 80)
    'reject'
    >>> decide_admission(85, 80)
    'accept with scholarship'
    >>> decide_admission(81, 80)
    'accept'
    """
    
    if average > cutoff:
        if average >= cutoff + 5:
            return ADMISSION_SCHOLARSHIP
        else:
            return ADMISSION_ACCEPTED
    else:
        return ADMISSION_REJECTED
    