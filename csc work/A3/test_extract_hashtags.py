import unittest
import tweets


class TestExtractHashtags(unittest.TestCase):

    def test_no_hashtags(self):
        """ Test extract_hashtags with a tweet with no hashtags. """

        actual_hashtags = tweets.extract_hashtags('this is a tweet!')
        expected_hashtags = []
        self.assertEqual(actual_hashtags, expected_hashtags, 'empty list')

    # Place your unit test definitions after this line.
    
    def test_all_hashtags(self):
        """ Test extract_hashtags with a tweet of nothing but hashtags. """
        
        actual_hashtags = tweets.extract_hashtags('#MAGA #Vote2016 #FeelTheBern')
        expected_hashtags = ['MAGA', 'Vote2016', 'FeelTheBern']
        self.assertEqual(actual_hashtags, expected_hashtags, 'only hashtags')
        
    def test_normal_tweet(self):
        """ Test extract_hashtags with a normal tweet including 
        two identical hashtags. """
        
        actual_hashtags = tweets.extract_hashtags('Go vote! #MAGA, #MAGA')
        expected_hashtags = ['MAGA']
        self.assertEqual(actual_hashtags, expected_hashtags, 'normal tweet')
        
    def test_abnormal_tweet(self):
        """ Test extract_hashtags with a poorly formatted tweet including
        multiple poorly formatted hashtags. """
        
        actual_hashtags = tweets.extract_hashtags('#MAGA abcd #abc@aa@#abcd^^^')
        expected_hashtags = ['MAGA', 'abc', 'abcd']
        self.assertEqual(actual_hashtags, expected_hashtags, 'abnormal tweet')

# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
