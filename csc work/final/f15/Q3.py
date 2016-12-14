# each case has errors. explain the errors in each case. (4 MARKS)

def case_1():
    cats = ['Fluffy', 'Mittens']
    message = 'I love ' + cats[1:]
    print(message)
    
    # You cannot concatenate a string ('I love') and a list (cats[1:].

def case_2():
    animals_to_foods = {'cat': 'kibble', \
            'dog': 'bones', 'horse': 'hay'}
    animals_to_foods['cat'] = 'tuna'
    print(animals_to_foods[0])
    
    # 0 is not a key in the dictionary animals_to_foods, and/or dicts don't
    # have indices.

def case_3():
    ages = [22, 19, 23, 18, 34, 31, 20]
    ages = ages.sort()
    print(ages[0])
    
    # ages.sort() returns a NoneType object.

def case_4():
    words = ['waffle', 'pancake', 'omelette']
    for word in words:
        word[0] = word[0].upper()
    print(words)
    
    # strings are immutable.
