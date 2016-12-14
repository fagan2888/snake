def build_username_to_mention_count(tweet_list):
    # complete the function body (7 MARKS)
    ''' (list of str) -> dict of {str: int}
    
    Return a dictionary where each key is a username mentioned in tweet_list
    and each value is the total number of times this username was mentioned in
    all of the tweets in tweet_list.
    
    >>> tweets = ['hi @me and @you', '@me yesterday', 'i saw @you', '@yo @you there']
    >>> d = build_username_to_mention_count(tweets)
    >>> d == {'yo': 1, 'me': 2, 'you': 3}
    True
    '''
    
    dictionary = {}
    for i in range(len(tweet_list)):
        data = tweet_list[i].split()
        for j in range(len(data)):
            item = data[j]
            mention = item[1:]
            if item[0] == '@':
                if mention not in dictionary:
                    dictionary[mention] = 0
                dictionary[mention] += 1
    return dictionary
    
def invert_dictionary(d):
    ''' dict of {str: int} -> dict of {int: str}
    
    Precondition: the values in d's key/value pairs are all different
    
    Return a new dictionary that is the inverse of d. (See example below.)
    
    >>> d = invert_dictionary({'me': 2, 'yo': 1, 'you': 3})
    >>> d == {2: 'me', 1: 'yo', 3: 'you'}
    True
    '''
    new_dict = {}
    for key in d:
        new_dict[d[key]] = key
    return new_dict

def most_mentioned_username(tweet_list):
    # complete the function body (4 MARKS)
    ''' (list of str) -> str
    Preconditions:
    - at least one of the strings in tweet_list will include a mention
    - each username mentioned in tweet_list will have a unique total number
    of mentions in tweet_list (i.e., no ties for the number of mentions)
    
    Return the username with the most mentions in tweet_list.
    
    >>> tweets = ['hi @you there', '@me yesterday', 'saw @you']
    >>> most_mentioned_username(tweets)
    'you'
    '''
    inverted = invert_dictionary(build_username_to_mention_count(tweet_list))
    largest = max(list(inverted.keys()))
    return inverted[largest]