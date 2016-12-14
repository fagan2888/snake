import Q10

class MessengerChat:
    ''' Information about a Messenger chat. '''
    
    def __init__(self, chat_id, chat_initiator):
        # complete the function body (1 MARK)
        ''' (MessengerChat, int, MessengerUser) -> NoneType
        
        Initialize a new Messenger chat that has chat id chat_id and a list
        of members that initially only contains chat_initiator.
        
        >>> user1 = MessengerUser('tom')
        >>> chat1 = MessengerChat(201, user1)
        >>> chat1.chat_id
        201
        >>> chat1.chat_members == [user1]
        True
        '''
        self.chat_id = chat_id
        self.chat_members = [chat_initiator]
    
    def add_member(self, potential_member):
        # complete the function body (2 MARKS)
        ''' (MessengerChat, MessengerUser) -> bool
        
        Precondition: All existing members of this MessengerChat are friends
        with at least one other member, or the chat contains only the chat 
        initiator. There is at least one member in the MessengerChat.
        
        Return True iff potential_member can be added to this chat, and if so,
        modify this MessengerChat's chat_members to add potential_member
        to the chat. A MessengerUser can be added to this chat if and only if
        they are friends with at least one other member of the chat.
        
        >>> user1 = MessengerUser('tom')
        >>> user1.friends.extend(['paul', 'jen'])
        >>> user2 = MessengerUser('jen')
        >>> user2.friends.extend(['tom', 'paul'])
        >>> user3 = MessengerUser('max')
        >>> user3.friends.extend(['paul'])
        >>> chat1 = MessengerChat(201, user1)
        >>> chat1.add_member(user2)
        True
        >>> chat1.chat_members == [user1, user2]
        True
        >>> chat1.add_member(user3)
        False
        >>> chat1.chat_members == [user1, user2]
        True
        '''
        for member in self.chat_members:
            if member.are_friends(potential_member):
                self.chat_members.append(potential_member)
                return True
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()