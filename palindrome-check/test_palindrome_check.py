import unittest
from palindrome_check import check_palindrome

class PalindromeCheckTestCase(unittest.TestCase):

    def test_palindrome_checking(self):
        self.assertTrue(check_palindrome('xex'))
        self.assertTrue(check_palindrome('kAjaK'))
        self.assertTrue(check_palindrome('poiuyttyuiop'))
        self.assertTrue(check_palindrome('RoMMor'))
        self.assertTrue(check_palindrome('wrakkarw'))
        self.assertTrue(check_palindrome('xx ffff xx'))
        self.assertTrue(check_palindrome('dd ee ee dd'))

        self.assertFalse(check_palindrome('wrak'))
        self.assertFalse(check_palindrome('konstantynopol'))
        self.assertFalse(check_palindrome('doner kebab'))
        self.assertFalse(check_palindrome('ala ma kota na punkcie kotow'))
        self.assertFalse(check_palindrome('halo odbjur'))
        self.assertFalse(check_palindrome(''))
        self.assertFalse(check_palindrome('h'))        
        

### 

unittest.main()