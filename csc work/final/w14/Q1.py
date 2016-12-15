def c_1():
    L = [4, 10, 8]
    x = L.sort()
    L.append(20)
    L2 = L[1:]
    
    # output:
    # >>> x
    # None
    # >>> L
    # [4, 8, 10, 20]
    # >>> id(L) == id(L2)
    # False

def repeat_word(word, num_times):
    ''' (str, int) -> str
    '''
    print(__name__)
    word = word * num_times
    print('Repeated word is:', word)
    return word

if __name__ == '__main__':
    word = 'Yes'
    print('Original word is:', word)
    repeat_word(word, 3)
    print('New word is:', word)
    word = repeat_word(word, 2) + '!'
    print('New word is:', word)
    
    # output:
    # Original word is: Yes
    # __main__
    # Repeated word is: YesYesYes
    # New word is: Yes
    # __main__
    # Repeated word is: YesYes
    # New word is: YesYes!