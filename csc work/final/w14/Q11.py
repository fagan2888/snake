# let k = len(L), specify the num of times 'happy!' is printed
# and the complexity. (5 MARKS)

def c_1():
    for i in range(len(L)):
        print('happy!')
    for item in L:
        print('happy!')
    
    # num of times 'happy!' is printed: 2k
    # complexity: linear

def c_2():
    for i in range(len(L)):
        for item in L[:i]:
            print('happy!')
    
    # num of times 'happy!' is printed: 0 + 1 + ... + (k - 1) = ((k-1)k)/2
    # complexity: quadratic
    
def c_3():
    # Precondition: len(L) % 10 == 0
    i = 0
    while i < len(L):
        print('happy!')
        i = i + len(L) // 10
    
    # num of times 'happy!' is printed: 10
    # complexity: constant
    

def c_4():
    for item in L[1000:2000]:
        print('happy!')
        
    # num of times 'happy!' is printed: 1000
    # complexity: constant

def c_5():
    for item in L[10:]:
        print('happy!')
    
    # num of times 'happy!' is printed: k - 10
    # complexity: linear
