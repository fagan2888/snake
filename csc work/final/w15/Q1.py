def code_1():
    L = [8, 12, 3]
    X = L.sort()
    Y = L[:]
    L.extend([1])
    
    print(X)
    print(id(Y) == id(L))
    print(L)
    
    #output:
    # None
    # False
    # [8, 12, 3, 1]
    
def code_2():
    for i in range(2):
        for j in range(2):
            print('{0}, {1}'.format(i, j))
    
    # output:
    # 0, 0
    # 0, 1
    # 1, 0
    # 1, 1
    
def find_bias(lst):
    ''' (list of int) -> int
    '''
    bias = 0
    for num in lst:
        if num % 2 == 0:
            return bias + 1
        else:
            return bias - 1
    return bias

def func(word):
    print(__name__)
    word = word + 'Na'
    print('0:', word)
    return word
    # return does not print.

def f1(x, y):
    print('f1:', x, y)
    return x + y
    # last 'return' will return the value

def f2(x, y):
    print('f2:', x, y)
    return x * y
    
def f(x):
    if x % 2 != 0:
        if x ** 2 <= 36:
            return 'Pow'
        else:
            return x // 3
    else:
        if x < 0 and abs(x) > 5:
            return False
        elif not x + 2 > 8:
            return x / 2
    return 'Zonk'

# f(2)
# 1.0
# (return type: str)

# f(13)
# 4
# (return type: int)

# f(-8)
# False
# (return type: bool)

# f(10)
# Zonk
# (return type: str)
    

if __name__ == '__main__':
    #my_list = [2, 4, 5, 6]
    #print('The even/odd bias is:', find_bias(my_list))
    
    # output:
    # The even/odd bias is: 1
    
    # word = 'Hey'
    # print('1:', word)
    # func(word)
    # print('2:', word)
    # word = func(word) + '!'
    # print('3:', word)
    
    # output:
    # 1: Hey
    # __main__
    # 0: HeyNa
    # 2: Hey
    # __main__
    # 0: HeyNa
    # 3: HeyNa!
    
    print (f1(f2(6, 5), f1(2, 4)))
    
    # output:
    # f2: 6, 5
    # f1: 2, 4
    # f1: 30, 6
    # 36