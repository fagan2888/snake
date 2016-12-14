# print output or state the error (5 MARKS)

def c_1():
    L1 = [1, 2, 3]
    L2 = [L1, L1]
    print(L2)
    
    # output:
    # [[1, 2, 3], [1, 2, 3]]

def c_2():
    L3 = [1, 2, 3]
    L4 = [L3, L3]
    L3.append(4)
    print(L4)
    
    # output:
    # [[1, 2, 3, 4], [1, 2, 3, 4]]

def c_3():
    s = 'hello'
    L5 = [s, s]
    s = 'hello' + ' there'
    print(L5)
    
    # output:
    # ['hello', 'hello']

def c_4():
    D1 = {}
    D1['a'] = 1
    D1['b'] = 2
    D1['a'] = 3
    print(len(D1))
    
    # output:
    # 2

def c_5():
    D1 = {1: 'hi', 2: 'bye'}
    print(D2[-1])
    
    # error: -1 is not a key in dictionary D1.
