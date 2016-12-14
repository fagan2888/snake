def can_fill_order(order_dict, inventory_dict):
    # complete the docstring description to show that 'can_fill_order
    # does not modify its parameters (2 MARKS)
    # complete the function body (8 MARKS)
    ''' (dict of {str: str}, dict of {str: int}) -> bool
    
    Return True iff the quantity (dict value) of every item (dict key) in 
    inventory_dict is greater than or equal to the quantity of the item ordered 
    in order_dict. If an item in order_dict is not in inventory_dict, 
    return False.
    
    >>> inventory = {'shirt': 2, 'mug': 2}
    >>> can_fill_order({'Ann': 'mug', 'Bob': 'mug', 'Lee': 'mug'}, inventory)
    False
    >>> can_fill_order({'Ann': 'shirt', 'Bob': 'mug', 'Lee': 'mug'}, inventory)
    True
    >>> can_fill_order({'Ann': 'mug', 'Bob': 'mug', 'Lee': 'hat'}, inventory)
    False
    >>> inventory = {'shirt': 2, 'mug': 2}
    >>> order = {'Ann': 'mug', 'Bob': 'mug'}
    >>> result = can_fill_order(order, inventory)
    >>> order == {'Ann': 'mug', 'Bob': 'mug'}
    True
    >>> inventory == {'shirt': 2, 'mug': 2}
    True
    '''
    
    order_counts = {}
    for entry in order_dict:
        if order_dict[entry] not in order_counts:
            order_counts[order_dict[entry]] = 0
        order_counts[order_dict[entry]] += 1
        
    for key in order_counts:
        if key not in inventory_dict or order_counts[key] > inventory_dict[key]:
            return False
    return True
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()