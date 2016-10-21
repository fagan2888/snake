def f(a,b):
    return a < 3 and not b
    
def g1(a, b):
    if a >= 3 or b:
        return False
    else:
        return True
        
def g2(a, b):
    if a < 3:
        return not b
        
def g3(a,b):
    if 3 > a and not b:
        return True
    else:
        return False

def g4(a,b):
    while a != 0:
        a = a - 1
    
    if a == 0:
        return not b 
        
    return False
    
def aer(i,j):
    sum = 0
    for val in range(i, j):
        if (val % 2) == 0:
            sum = sum + val
    return sum
    
def rem(s, c):
    if len(c) == 1:
        return s.replace(c + c + c, c)
        

def ff(num):
    num = num + 2
    if num < 0:
        return num * -1
    return num

def excc(course):
    i = course.index(':')
    return course[i+2: i + 11]
    
def dtl(items):
    result = []
    for val in items:
        result.append(val)

    for val in items:
        result.append(val)
    return result
    
