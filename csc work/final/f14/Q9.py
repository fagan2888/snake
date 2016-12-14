class Review:
    ''' A review of a restaurant. '''
    
    def __init__(self, reviewer_name, review_comments, is_recommended):
        ''' (Review, str, str, bool) -> NoneType
        
        Record the reviewer's name reviewer_name, the reviewer's comments
        review_comments, and the reviewer's recommendation is_recommended.
        
        >>> review = Review('Lynn Crawford', 'Delicious food!', True)
        >>> review.reviewer
        'Lynn Crawford'
        >>> review.comments
        'Delicious food!'
        >>> review.recommend
        True
        '''
        
        self.reviewer = reviewer_name
        self.comments = review_comments
        self.recommend = is_recommended
    
    def change_comments(self, new_comments):
        ''' (Review, str) -> NoneType
        Update the comments for this review to new_comments
        '''
        self.comments = new_comments
    
    def __str__(self):
        ''' (Review) -> str
        
        Return a string representation of this review.
        >>> review = Review('Susur Lee', 'Excellent!', True)
        >>> str(review)
        'recommended by Susur Lee: Excellent!'
        >>> review = Review('Mark McEwan', 'Room for improvement.', False)
        >>> str(review)
        'not recommended by Mark McEwan: Room for improvement.'
        '''
        
        recommend = 'not recommended'
        if self.recommend:
            recommend = 'recommended'
        return '{0} by {1}: {2}'.format(recommend, self.reviewer, self.comments)