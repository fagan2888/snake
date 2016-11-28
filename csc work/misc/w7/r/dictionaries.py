def express_checkout(product_to_quantity):
    """ (dict of {str: int}) -> bool

    Return True iff the grocery order in product_to_quantity qualifies for the
    express checkout.  product_to_quantity maps products to the numbers of those
    items in the grocery order.
    
    The express checkout is for orders of 8 items or fewer.

    >>> express_checkout({'banana': 3, 'soy milk': 1, 'peanut butter': 1})
    #TODO: Complete return value of above function call.
    >>> express_checkout({'banana': 3, 'soy milk': 1, 'twinkie': 5})
    #TODO: Complete return value of above function call.
    """
    
    item_count = 0
    for key in product_to_quantity:
        item_count += product_to_quantity[key]
    
    return item_count <= 8
    
def build_placements(shoes):
    """ (list of str) -> dict of {str: list of int}

    Return a dictionary where each key is a shoe company from shoes and each value is a
    list of placements by people wearing footwear made by that company. First place is at index
    0 of shoes, 2nd place is at index 1, and so on.

    >>> build_placements(['Saucony', 'Asics', 'Asics', 'NB', 'Saucony', \
                          'Nike', 'Asics', 'Adidas', 'Saucony', 'Asics'])
    {'Saucony': [1, 5, 9] 'Asics': [2, 3, 7, 10], 'NB': [4], 'Nike': [6], 'Adidas': [8]}                      
    """
    
    placements = {}
    position = 1
    for item in shoes:
        if item not in placements:
            placements[item] = []
        placements[item].append(position)
        position += 1
    return placements
    