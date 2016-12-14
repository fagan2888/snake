def f1():
    month = 'April'
    date = 23
    today = month + '' + date
    
    # error:
    # cannot concatenate str (month) and int (date)

def f2():
    seasons = ['Winter', 'Spring', 'Summer', 'Fall']
    terms = seasons[:]
    terms.upper()
    
    # error:
    # type list has no method 'upper'
    
def f3():
    ['2015', 'September'].extend(4)
    
    # error:
    # extend requires an iterable (list) as an argument

def f4():
    department = 'Computer Science'
    faculty = [9:]
    faculty = faculty + [' 2015']
    
    # error:
    # cannot concatenate string and list