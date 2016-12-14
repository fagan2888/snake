HIT = 'X'
MISS = 'M'

def count_hits_and_misses(board):
    ''' (list of list of str) -> list of int
    Precondition: board != [] and each list in board has len(board)
    
    Return a list that contains the number of occurrences of the
    HIT or MISS symbol in each row of board.
    
    >>> board = [['-','M','-'], ['X','M','-'], ['-','-','-']]
    >>> count_hits_and_misses(board)
    
    [1, 2, 0]
    '''
    count = [0, 0, 0]
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            if row[j] != '-':
                if row[j] == HIT:
                    count[0] += 1
                elif row[j] == MISS:
                    count[1] += 1
    return count
