class MessengerUser:
    ''' Information about a particular Messenger user. '''
    
    def __init__(self, messenger_username):
        # complete the body (1 MARK)
        ''' (MessengerUser, str) -> NoneType
        
        Initialize a new Messenger user that has username messenger_username,
        and an empty friends list.
        >>> user1 = MessengerUser('tom')
        >>> user1.username
        'tom'
        >>> user1.friends
        []
        '''
        self.username = messenger_username
        self.friends = []
    
    def __str__(self):
        # complete the body (2 MARKS)
        ''' (MessengerUser) -> str
        
        Return a string representation of this Messenger user.
        
        >>> user1 = MessengerUser('tom')
        >>> user1.friends.append('jen')
        >>> print(user1)
        User tom has 1 friend(s).
        >>> user2 = MessengerUser('jen')
        >>> user2.friends.extend(['paul', 'tom'])
        >>> print(user2)
        User jen has 2 friend(s).
        '''
        return 'User ' + self.username + ' has ' + \
                    str(len(self.friends)) + ' friend(s).'
    
    def are_friends(self, other_user):
        ''' (MessengerUser, MessengerUser) -> bool
        
        Return True iff this MessengerUser and other_user are friends.
        
        >>> user1 = MessengerUser('tom')
        >>> user1.friends.extend(['jen', 'paul'])
        >>> user2 = MessengerUser('jen')
        >>> user2.friends.extend(['tom', 'paul'])
        >>> user3 = MessengerUser('paul')
        >>> user3.friends.extend(['jen'])
        >>> user1.are_friends(user2)
        True
        >>> user1.are_friends(user3)
        False
        '''
        
        return (self.username in other_user.friends) and \
                (other_user.username in self.friends)

if __name__ == '__main__':
    import doctest
    doctest.testmod()