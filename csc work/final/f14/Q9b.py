import Q9

class Restaurant:
    ''' Information about a particular restaurant inclduing its name,
    price range, the types of cuisines it serves, and reviews.'''
    
    def __init__(self, name, price_range, cusine_list):
        ''' (Restaurant, str, str, list of str) -> NoneType
        Record the restaurant's name name, price range price_range, and 
        types of cuisines cuisines_list. There are initially no reviews of 
        this restaurant.
        
        >>> rest = Restaurant('Dumplings R Us', '$$', ['Chinese', 'Japanese'])
        >>> rest.name
        'Dumplings R Us'
        >>> rest.price_range
        '$$'
        >>> rest.cuisine_list
        ['Chinese', 'Japanese']
        >>> rest.reviews
        []
        '''
        self.name = name
        self.price_range = price_range
        self.cusine_list = cusine_list
        self.reviews = []
        
    def add_review(self, review):
        ''' (Restaurant, Review) -> NoneType
        
        >>> rest = Restaurant('Mexican Grill', '$$$', ['Mexican'])
        >>> rest.reviews
        []
        >>> review = Review('Susur Lee', 'Excellent!', True)
        >>> rest.add_review(review)
        >>> str(rest.reviews[0])
        'recommended by Susur Lee: Excellent!'
        '''
        self.reviews.append(review)
    
    def __eq__(self, other):
        ''' (Restaurant, Restaurant) -> bool
        Return whether this restaurant has the same name and price range
        as other.
        
        >>> r1 = Restaurant('Dumplings R Us', '$$', ['Chinese', 'Japanese'])
        >>> r2 = Restaurant('Dumplings R Us', '$$', ['Chinese', 'Japanese'])
        >>> r3 = Restaurant('Deep Fried Everything', '$', ['Canadian'])
        >>> r1 == r2
        True
        >>> r2 == r3
        False
        '''
        
        return self.name == other.name and self.price_range == other.price_range
    
    def recommended_percentage(self):
        ''' (Restaurant) -> number
        Precondition: this restaurant has at least one review
        
        Return the percentage of reviews that recommend this restaurant.
        
        >>> rest = Restaurant('Mexican Grill', '$$$', ['Mexican'])
        >>> rest.add_review(Review('Susur Lee', 'Excellent!', True))
        >>> rest.add_review(Review('Mark McEwan', 'Room for improvement.', False))
        >>> rest.recommended_percentage()
        50.0
        '''
        num_of_reviews = len(self.reviews)
        count = 0
        for review in self.reviews:
            if review.recommend == True:
                count += 1
            #num_of_reviews += 1
        return (count / num_of_reviews) * 100
