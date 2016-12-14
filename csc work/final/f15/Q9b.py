import Q9

class SkypeCall:
    ''' Information about a Skype call. '''
    
    def __init__(self, call_id, call_initiator):
        ''' (SkypeCall, int, SkypeUser) -> NoneType
        
        Initialize a SkypeCall with a call id call_id and a list of members
        that initially only contains Skype user call_initiator.
        
        >>> user1 = SkypeUser('uoft123', 'Toronto', ['debbie'])
        >>> call1 = SkypeCall(201, user1)
        >>> call1.call_id
        201
        >>> call1.call_members == [user1]
        True
        '''
        
        self.call_id = call_id
        self.call_members = [call_initiator]
        
    def add_members(self, potential_members):
        ''' (SkypeCall, list of SkypeUser) -> int
        
        Precondition: All existing members of this Skype call share the same
        location and there is at least one member in the call.
        
        Add call members from potential_members to this Skype call and return
        the number of newly added call members.
        
        A person from potential_members can only be added to this call if
        their location is the same as the location of all the other members of
        that call.
        
        >>> user1 = SkypeUser('uoft123', 'Toronto', ['debbie'])
        >>> user2 = SkypeUser('mel', 'Vancouver', [])
        >>> user3 = SkypeUser('max', 'Toronto', [])
        >>> call1 = SkypeCall(201, user1)
        >>> call1.add_members([user2, user3])
        1
        >>> # only Skype user with username max was added.
        '''
        count = 0
        for user in potential_members:
            if user.location == self.call_members[0].location:
                self.call_members.append(user)
                count += 1
        return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()