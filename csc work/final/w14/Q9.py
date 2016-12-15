def populate_dictionary(definition_file):
    # complete the body of the function. do not use methods read
    # or readlines, and do not use for loops. instead, use while and
    # method readline. (9 MARKS)
    ''' (file open for reading) -> dict of {str: list of str}
    
    Preconditions:
    - definition_file contains 0 or more entries with the following format:
    - 1 line containing a word
    - 0 or more lines with a definition of that word (one definition per line)
    - there will be one blank line between entries
    
    Return a dictionary where each key is a word and each value is the list of
    definitions of that word from definition_file. Even if a word has 0 definitions,
    it should appear as a key in the dictionary.
    '''
    
    # dictionary = {}
    # line = definition_file.readline().strip()
    # while line != '':
    #     if len(line.split()) == 1:
    #         word = line.strip()
    #         dictionary[word] = []
    #         line = definition_file.readline()
    #         while len(line.split()) != 1:
    #             dictionary[word].append(line)
    #             line = definition_file.readline()
    # return dictionary
    
    word_to_definitions = {}
    word = definition_file.readline().strip()
    
    while (word!= ''):
        word_to_definitions[word] = []
        definition = definition_file.readline().strip()
        while (definition != ''):
            word_to_definitions[word].append(definition)
            definition = definition_file.readline().strip()
        word = definition_file.readline().strip()
    return word_to_definitions
