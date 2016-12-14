def statement_1():
    food_to_count = {'burger': 3, \
            'fries': 5, 'salad' : 7}
    food_to_count['salad'] = 1
    print(food_to_count[2])
    
    # 2 is not a key in the dictionary. Furthermore, dictionaries
    # don't have indices.

def statement_2():
    foods = ['soup', 'waffle', 'pizza']
    for food in foods:
        food[0] = food[0].upper()
    print(foods)
    
    # strings aren't mutable.

def statement_3():
    grades = [75, 68, 82]
    grades = grades.extend([90])
    print(grades[-1])
    
    # extend returns a NoneType (it is an instance method, not a class method)
    # so it doesn't return anything.

def statement_4():
    full_name = ['Jovi', 'Jon', 'Bon']
    name = full_name[1:] + full_name[0]
    print(name)
    
    # cannot concatenate two different types (list and string), for this we
    # need to use append.
    
def statement_5():
    names_to_ages = \
            {['Ann', 'Lee']: [21, 19]}
    names_to_ages['Fan'] = 22
    print(names_to_ages)
    
    # cannot use list as a key in dictionary names_to_ages, since dictionary
    # keys must of some immutable type.
    
def statement_6():
    filename = 'data.txt'
    file_lines = filename.readlines()
    print(file_lines[-1])
    
    # we cannot call filename.readlines() since we haven't opened the file
    # filename, which is of type str. need to be called on a file.
    # i.e. call file = open(filename, 'r')