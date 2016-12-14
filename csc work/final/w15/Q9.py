def bark_like_a_dog(L):
    ''' (list of object) -> NoneType
    '''
    for item in L:
    print('Woof!')
    
    # len(L) = n
    # prints 'Woof!' n-many times. dependence on n is linear.
    
def c_1():
    i = 0
    while i < len(L):
        bark_like_a_dog(L[i:i + 1])
        i += 1
    
    # prints 'Woof!' n-many times. dependence on n is linear.

def c_2():
    i = 0
    while i < len(L):
        bark_like_a_dog[L[i:]
        i += 1
    
    # prints 'Woof!' n + (n -1) + (n - 2) + .. + 1 = 1 + 2 + ... + n
    # = n(n+1)/2, approx (n^2)/2
    # dependence on n is quadratic.

def c_3():
    i = 0
    while not(i < len(L)):
        bark_like_a_dog(L)
        i += 1
    
    # prints 'Woof!' 0 times. dependence on n is constant.
