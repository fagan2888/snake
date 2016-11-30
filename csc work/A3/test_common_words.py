import unittest
import tweets


class TestCommonWords(unittest.TestCase):

    def test_none_removed(self):
        """ Test common_words with N so that no words are removed. """

        words_to_counts = {'cat': 1}
        expected_result = {'cat': 1}
        tweets.common_words(words_to_counts, 1)
        self.assertEqual(words_to_counts, expected_result, 'none removed')

    # Place your unit test definitions after this line.
    
    def test_identical_counts_smaller_N(self):
        """ Test common_words where all counts are identical and N is
        smaller than the length of the dictionary. """
        
        words_to_counts = {'cat': 5, 'hat': 5, 'mat': 5, 'rat': 5, 'fat': 5}
        expected_result = {}
        tweets.common_words(words_to_counts, 4)
        self.assertEqual(words_to_counts, expected_result, 'identical count #1')
        
    def test_identical_counts_equal_N(self):
        """ Test common_words where all counts are identical and N is
        smaller than the length of the dictionary. """
        
        words_to_counts = {'cat': 5, 'hat': 5, 'mat': 5, 'rat': 5, 'fat': 5}
        expected_result = {'cat': 5, 'hat': 5, 'mat': 5, 'rat': 5, 'fat': 5}
        tweets.common_words(words_to_counts, 5)
        self.assertEqual(words_to_counts, expected_result, 'identical count #2')
        
    def test_lower_bound_larger(self):
        """ Tests common_words where the Nth possible item has duplicates. """
        
        words_to_counts = {'cat': 4, 'hat': 5, 'mat': 5, 'rat': 6, 'fat': 7}
        expected_result = {'rat': 6, 'fat': 7}
        tweets.common_words(words_to_counts, 3)
        self.assertEqual(words_to_counts, expected_result, 'lower bound #1')
    
    def test_lower_bound_smaller(self):
        """ Tests common_words where the duplicates fit within the N spaces. """
        
        words_to_counts = {'cat': 4, 'hat': 5, 'mat': 5, 'rat': 6, 'fat': 7}
        expected_result = {'rat': 6, 'fat': 7, 'mat': 5, 'hat': 5}
        tweets.common_words(words_to_counts, 4)
        self.assertEqual(words_to_counts, expected_result, 'lower bound #2')
        
    def test_upper_bound_larger(self):
        """ Tests common_words where the count of the largest item is within
        the N spaces. """
        
        words_to_counts = {'cat': 4, 'hat': 5, 'mat': 7, 'rat': 7, 'fat': 7}
        expected_result = {'hat': 5, 'mat': 7, 'rat': 7, 'fat': 7}
        tweets.common_words(words_to_counts, 4)
        self.assertEqual(words_to_counts, expected_result, 'upper bound #1')
    
    def test_upper_bound_smaller(self):
        """ Tests common_words where the count of the largest item exceeds
        the N spaces. """
        
        words_to_counts = {'cat': 4, 'hat': 7, 'mat': 7, 'rat': 7, 'fat': 7}
        expected_result = {}
        tweets.common_words(words_to_counts, 3)
        self.assertEqual(words_to_counts, expected_result, 'lower bound #2')

# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
