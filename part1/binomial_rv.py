from random import uniform

def binomial_rv(n, p):
    ''' (int, int) -> int
    Returns a random draw from Bin(n, p) for n an integer, p in (0, 1).
    '''
    
    count = 0
    for i in range(n):
        u = uniform(0, 1)
        if u < p:
            count += 1
    return count

binomial_rv(10, 0.5)
