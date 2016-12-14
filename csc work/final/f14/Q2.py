def shift_right(L):
    temp = L[len(L) - 1]
    for i in range(len(L) - 1, 0, -1):
        L[i] = L[i - 1]
    L[0] = temp

def shift_left(L):
    temp = L[0]
    for i in range(len(L) - 1):
        L[i] = L[i + 1]
    L[len(L) - 1] = temp
