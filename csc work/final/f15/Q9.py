class SkypeUser:
    ''' Information about a particular Skype user. '''
    
    def __init__(self, skype_username, skype_location, skype_contacts):
        ''' (SkypeUser, str, str, list of str) -> NoneType
        
        Initialize a new Skype user that has username skype_username,
        location skype_location and contacts skype_contacts
        >>> user1 = SkypeUser('uoft123', 'Toronto', ['debbie', 'paul'])
        >>> user1.username
        'uoft123'
        >>> user1.location
        'Toronto'
        >>> user1.contacts
        ['debbie', 'paul']
        '''
        self.username = skype_username
        self.location = skype_location
        self.contacts = skype_contacts
        
    def __str__(self):
        ''' (SkypeUser) -> str
        
        Return a string representation of this Skype user.
        >>> user1 = SkypeUser('uoft123', 'Toronto', ['debbie'])
        >>> print(user1)
        uoft123 lives in Toronto and has 1 contact(s).
        >>> user2 = SkypeUser('mel', 'Vancouver', ['paul', 'debbie'])
        >>> print(user2)
        mel lives in Vancouver and has 2 contact(s).
        '''
        
        return '{0} lives in {1} and has {2} contact(s).'.format(self.username, \
                self.location, len(self.contacts))
    
    def same_contacts(self, user_contacts):
        # complete the method body (2 MARKS)
        ''' (SkypeUser, list of str) -> 
        
        Return True iff this Skype user has the same contacts, in any order,
        as the ones in user_contacts. The elements in user_contacts and
        the contacts of this Skype user may be reordered.
        
        >>> user1 = SkypeUser('uoft123', 'Toronto', ['debbie', 'paul'])
        >>> contact_list1 = ['paul', 'debbie']
        >>> contact_list2 = []
        >>> user1.same_contacts(contact_list1)
        True
        >>> user1.same_contacts(contact_list2)
        False
        '''
        return sorted(self.contacts) == sorted(user_contacts)

    def __eq__(self, other_user):
        ''' (SkypeUser, SkypeUser) -> bool
        Return True iff this Skype user has the same contacts as
        Skype user other_user.
        >>> user1 = SkypeUser('uoft123', 'Toronto', ['debbie', 'paul'])
        >>> user2 = SkypeUser('mel', 'Vancouver', ['paul', 'debbie'])
        >>> user1 == user2
        True
        >>> user3 = SkypeUser('uoft_cs1', 'Toronto', \
        ['debbie', 'ioana', 'alex', 'paul'])
        >>> user1 == user3
        False
        '''
        return self.same_contacts(other_user.contacts)

if __name__ == '__main__':
    import doctest
    doctest.testmod()