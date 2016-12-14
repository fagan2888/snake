import unittest
import sum

class TestSumValues(unittest.TestCase):
    
    def test_last_digit(self):
        """ Test 'sum values' where only the last digit
        is above the threshold. """
        
        values = '1234'
        expected_result = 4
        obtained = sum.sum_values_above_threshold(values, 3)
        self.assertEqual(obtained, expected_result)
    
    # Add three more test cases (3 MARKS):
    
    def test_above_threshold(self):
        """ Test a multi-character string, all above the threshold. """
        
        values = '99999'
        expected_result = 45
        obtained = sum.sum_values_above_threshold(values, 8)
        self.assertEqual(obtained, expected_result)
        
    def test_below_threshold(self):
        """ Test a multi-character string, all above the threshold. """
        
        values = '88888'
        expected_result = 0
        obtained = sum.sum_values_above_threshold(values, 9)
        self.assertEqual(obtained, expected_result)
        
    def test_single_char_threshold(self):
        """ Test a single character string above the threshold. """
        
        values = '2'
        expected_result = 2
        obtained = sum.sum_values_above_threshold(values, 1)
        self.assertEqual(obtained, expected_result)

if __name__ == '__main__':
    unittest.main(exit=False)