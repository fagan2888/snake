valid_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_'
numbers = '0123456789'
candidates = ['Donald Trump', 'Secretary Hillary Clinton', 
'Governor Gary Johnson', 'Dr. Jill Stein']

def extract_mentions(text):
    ''' (str) -> list of str
    
    Returns a list of strings representing the twitter usernames
    mentioned in the tweet's text, in the order they appear and including
    repeated mentions.
    Precondition: len(text) < 140
    
    >>> extract_mentions('@realDonaldTrump, @SenSanders, @HillaryClinton')
    ['realDonaldTrump', 'SenSanders', 'HillaryClinton']
    >>> extract_mentions('@realDonaldTrump #MAGA #MAGA #MAGA')
    ['realDonaldTrump']
    >>> extract_mentions('Voter recount? @SenSanders?')
    ['SenSanders']
    >>> extract_mentions('@realDonaldTrump abcdefg @realDonaldTrump')
    ['realDonaldTrump', 'realDonaldTrump']
    '''
    mentions = []
    tweet = text.split()
    
    for i in range(len(tweet)):
        if tweet[i][0] == '@':
            candidate_text = tweet[i][1:]
            mention = ''
            
            for i in range(len(candidate_text)):
                char = candidate_text[i]
                if char in valid_chars:
                    mention += char
                    
            mentions.append(mention)
    return mentions
    
def extract_hashtags(text):
    ''' (str) -> list of str
    
    Returns a list of strings representing the hashtags used in the
    tweet's text, in the order they appear and excluding repeats.
    Precondition: len(text) < 140
    
    >>> extract_hashtags('#MAGA #MAGA #MAGA @realDonaldTrump 2016!!!')
    ['MAGA']
    >>> extract_hashtags('#2016Election #Election2016 Go out and vote!')
    ['Election2016']
    >>> extract_hashtags('this tweet is full of errors #abc@aa@#abcd^^^')
    ['abc', 'abcd']
    '''
    
    hashtags = []
    tweet = text.split()
    # For entries in tweet which have multiple hashtag characters,
    # we parse through the entry, extracting all possible hashtags.
    
    tweet = helper_1(tweet)
    
    # For each entry in tweet, extract the hashtags.
    for i in range(len(tweet)):
        candidate = tweet[i]
        
        if candidate[0] == '#':
            candidate_text = candidate[1:]
            
            if candidate_text[1] not in numbers:
                hashtag = ''
                
                for i in range(len(candidate_text)):
                    char = candidate_text[i]
                    
                    if char in valid_chars:
                        hashtag += char
                    else:
                        break
                if hashtag not in hashtags:
                    hashtags.append(hashtag)
    return hashtags

def helper_1(tweet):
    ''' (list of str) -> list of str
    
    Returns a list of strings which are the former entries of the tweet list
    that have been formatted to split each occurence of '#' in each entry.
    
    >>> helper_1(['#abc@aa@#abcd^^^', '#abc'])
    ['#abc@aa@', '#abcd^^^', '#abc']
    '''
    new_tweet = []
    for i in range(len(tweet)):
        candidate = tweet[i]
        
        if candidate.count('#') > 1:
            candidate = candidate.replace('#', ' ')
            candidate_list = candidate.split()
            
            for i in range(len(candidate_list)):
                candidate_list[i] = '#' + candidate_list[i]
                new_tweet.append(candidate_list[i])
        else:
            new_tweet.append(candidate)
    return new_tweet
    
def count_words(text, dictionary):
    ''' (str, dict of {str, int}) -> None
    
    Modifies a dictionary of lowercase words as keys (which are words taken
    from the tweet text, made lowercase and stripped of non-alphanumeric
    characters. URLs are ignored) and their respective number of occurences 
    in the tweet text as their assigned values.
    
    >>> t = "@utmandrew Don't you wish you could vote? #MakeAmericaGreatAgain"
    >>> dict = {'you': 0, 'dont': 0, 'wish': 0, 'could': 0, 'vote': 0}
    >>> count_words(t, dict)
    >>> dict == {'vote': 1, 'could': 1, 'you': 2, 'dont': 1, 'wish': 1}
    True
    >>> t = "@realDonaldTrump CHECK this out! http://www.google.com"
    >>> dict = {}
    >>> count_words(t, dict)
    >>> dict == {'this': 1, 'check': 1, 'out': 1}
    True
    '''    
    
    illegal_chars = numbers + '_.,;{}[]+=-!$%^&*()`~?|\\/'
    tweet = text.split()
    tweet_words_final = []
    
    for i in range(len(tweet)):
        if tweet[i].startswith('http://'):
            break
        candidate = tweet[i].replace('\'', '').strip(illegal_chars).lower()
        
        if not (candidate[0] == '#' or candidate[0] == '@'):
            tweet_words_final.append(candidate)
            
    for word in tweet_words_final:
        if word not in dictionary:
            
            dictionary[word] = 0
        dictionary[word] += 1
        
def common_words(dictionary, N):
    ''' (dict of {str: int}, int) -> None 
    
    Modifies a dictionary of lowercase words (as in count_words) by only
    including the largest N-many words, for N a positive integer, as sorted 
    by their respective values. Note: If including the N-th word would yield
    a dictionary of length > N, then we omit including this word and any other
    words that share the same key and lower.
    
    >>> dictionary = {'a': 3, 'b': 3, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
    >>> common_words(dictionary, 5)
    >>> dictionary == {'e': 5, 'd': 4, 'f': 6, 'g': 7}
    True
    >>> dictionary2 = {'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3, 'f': 3, 'g': 3}
    >>> common_words(dictionary2, 5)
    >>> dictionary2 == {}
    True
    '''
    
    if N < len(dictionary.keys()):
        new_dict = dict(dictionary)
        
        for i in range(N):
            value = new_dict[max(new_dict, key=lambda i: new_dict[i])]
            key = list(new_dict.keys())[list(new_dict.values()).index(value)]
            num_occurences = helper_2(new_dict)[value]
            
            if (N - i) >= num_occurences:
                del new_dict[key]
                
        for key in new_dict:
            if key in dictionary:
                del dictionary[key]
    
def helper_2(dictionary):
    ''' (dict of {type1: type2}) -> (dict of type {type2: int})
    
    Returns a dictionary where the keys are the values of the argument
    dictionary, and the values are its frequency (number of occurences) in
    the argument dictionary.
    >>> dictionary = {'a': 1, 'b': 1, 'c': 2, 'd': 2, 'e': 3, 'f': 3, 'g': 3}
    >>> helper_2(dictionary) == {1: 2, 2: 2, 3: 3}
    True
    '''
    
    dict_count = {}
    for value in dictionary.values():
        if value not in dict_count:
            dict_count[value] = 0
        dict_count[value] += 1
    return dict_count

def read_tweets(file):
    ''' (file open for reading) -> dict of {str: list of tweet tuples}
    
    Returns a dictionary of candidates as keys and tweet information as values,
    where the tweet information is in the form of tweet tuples where each tuple
    represents data retrieved from a single tweet in the format:
    (candidate, tweet text, date, source, # favorites, # retweets).
    All info retrieved from a file of tweet data.
    Precondition: for each tweet tuple, the values for date, # favorites
    and # retweets should be of type int, while values for candidate and
    tweet text should be of type str.
    
    How do I doctest this?
    '''
    
    tweets = {}
    line = file.readline()
    while line != '':
        if line.strip()[:-1] in candidates:
            candidate = line.strip()[:-1]
            tweets[candidate] = []
            line = file.readline()
            
        data = line.split(',')
        if [type(data[i]) == int for i in [0, 1, 4, 5]]:
            del data[0], data[1]
            for i in [0, 2, 3]:
                data[i] = int(data[i])
        data.insert(0, candidate)
        line = file.readline()
        
        tweet_text = ''
        while line != '<<<EOT\n':
            tweet_text += line.strip() + ' '
            line = file.readline()
        data.insert(1, tweet_text)
        
        info = ()
        for i in range(len(data)):
            if type(data[i]) == int:
                info += data[i],
            else:
                info += data[i].strip(),
        tweets[candidate].append(info)
        line = file.readline()
    return tweets
    
def most_popular(tweets, start, end):
    ''' (dict of {str: list of tweet tuples}, int, int) -> str
    
    Returns a string representing the most popular candidate in the dictionary
    of tweets that have posted between the dates of start and end. Popularity
    is measured by the sum of favorites and retweets for each tweet written by
    the candidate between the two dates.
    '''
    # make an empty dictionary
    # for each key in tweets, make a sum = 0
    # for each tuple associated to the key, find the ones where
    # int1 <= tuple[2] <= int2 and add the RT and FAV count to the sum
    # enter the key and the final sum to the empty dictionary
    # return the key associated to the largest entry in the dictionary
    dict = {}
    for key, value in tweets.items():
        sum = 0
        tuples = tweets[key]
        for i in range(len(tuples)):
            if start <= tuples[i][2] <= end:
                sum += tuples[i][4] + tuples[i][5]
        if sum not in dict.values():
            dict[key] = sum
        else:
            result = 'Tie'
    top = dict[max(dict, key=lambda i: dict[i])]
    most_popular = list(dict.keys())[list(dict.values()).index(top)]
    if helper_3(dict, top) > 1:
        return 'Tie'
    return most_popular

def helper_3(collection, value):
    ''' (data of type dict or list, object of arbitrary type) -> int
    
    Returns the number of instances the entry value (of arbitrary type)
    occurs in collection, which is either a dict or a list.
    
    >>> helper_3(['a', 'b', 'a'], 'a')
    2
    >>> helper_3({1:2, 2:3, 1:3}, 3)
    2
    '''
    
    count = 0
    if type(collection) == dict:
        for key in collection:
            if collection[key] == value:
                count += 1
    elif type(collection) == list:
        for item in collection:
            if item == value:
                count += 1
    return count

def detect_author(tweets, tweet):
    ''' (dict of {str: list of tweet tuples}, str) -> str
    
    Returns the probable author of a tweet based on the tweets passed in
    as an argument (which is the output of read_tweets of some tweet data).
    Probable author is found by retrieving the hashtags found in the tweet
    and comparing that to each candidate's lists of all hashtags they've used
    and all unique hashtags they've used. If the hashtag is not unique, then
    the candidate who used that hashtag the most will be returned as the
    probable author.
    '''
    # check if the tweet string contains any hashtags. If not, return 'Unknown'
    # If there are hashtags, extract them from the tweet and into their own
    # list. create a new dictionary. now go through each key in the argument
    # dictionary. For each key in the old-dictionary (i.e. for each candidate),
    # get all their hashtags and assign that as the first tuple value for the 
    # candidate's key in the new dictionary. the second tuple entry should be
    # the candidate's unique hashtags. this is our candidate hashtag library.
    # Formal algorithm:
    # for each hashtag in the tweet argument hashtags, check if it appears in
    # the unique hashtags list for each candidate. If it does, then immediately
    # return that candidate. If not, check how many times that hashtag occurs
    # in the candidate's non-unique hashtag list. create a counter and add up
    # all the hashtag matches for each candidate for each hashtag. Make a third
    # dictionary matching the candidate to their hashtag count.
    # return the candidate with the highest hashtag count.
    
    tweet_hashtags = extract_hashtags(tweet)
    candidate_hashtags = {}
    counts = {}
    all_hashtags = helper_5(tweets)
    unique_hashtags = helper_4(all_hashtags)
    if tweet_hashtags != []:
        for key, value in tweets.items():
            candidate_hashtags[key] = (all_hashtags[key], unique_hashtags[key])
            counts[key] = 0
        for hashtag in tweet_hashtags:
            counter = 0
            for key, value in candidate_hashtags.items():
                if hashtag in candidate_hashtags[key][1]:
                    return key
                else:
                    counter += helper_3(candidate_hashtags[key][0], hashtag)
                    counts[key] += counter
        max_value = counts[max(counts, key=lambda i: counts[i])]
        author = list(counts.keys())[list(counts.values()).index(max_value)]
        return author
    else:
        return 'Unknown'

    
def helper_4(candidate_hashtags):
    '''
    Pass a dictionary of candidates as keys and their respective hashtags as
    their associated values. Returns a dictionary of candidates as keys and
    the candidates' unique hashtags as their respective values.
    '''
    
    unique_dict = {}
    for key, value in candidate_hashtags.items():
        unique_dict[key] = []
        candidate = candidate_hashtags[key]
        for i in range(len(candidate)):
            hashtag = candidate[i]
            for k in candidate_hashtags.keys():
                if k != key:
                    if hashtag not in candidate_hashtags[k]:
                        unique_dict[key].append(hashtag)
    return unique_dict

def helper_5(tweets):
    ''' 
    Pass a dictionary obtained from read_tweets. Returns a dictionary
    of candidates as keys and all the hashtags used by the candidate as their
    respective values.
    '''
    tweets_dict = {}
    for key, value in tweets.items():
        tweets_dict[key] = []
        tuples = tweets[key]
        for i in range(len(tuples)):
            tweets_dict[key] += extract_hashtags(tuples[i][1])
    return tweets_dict

if __name__ == '__main__':
    import doctest
    doctest.testmod()