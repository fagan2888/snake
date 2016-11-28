def digital_sum(nums_list):
    """ (list of str) -> int
    
    Precondition: s.isdigit() holds for each string s in nums_list.

    Return the sum of all the digits in all strings in nums_list.

    >>> digital_sum(['64', '128', '256'])
    34
    >>> digital_sum(['12', '3'])
    6
    """
    
    #total = 0
    #for num in nums_list:
    #    for char in num:
    #        total += int(char)
    #return total
    
    total = 0
    for i in range(len(nums_list)):
        for j in range(len(nums_list[i])):
            total += int(nums_list[i][j])
    return total
    
def can_pay_with_two_coins(denoms, amount):
    """ (list of int, int) -> bool
    
    Return True if and only if it is possible to form amount, which is a
    number of cents, using exactly two coins, which can be of any of the
    denominations in denoms.

    >>> can_pay_with_two_coins([1, 5, 10, 25], 35)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 20)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 12)
    #TODO: complete the example output

    """

    #TODO: complete the function body
    for i in range(len(denoms)):
        for j in range(len(denoms)):
            if denoms[i] + denoms[j] == amount:
                return True
    return False