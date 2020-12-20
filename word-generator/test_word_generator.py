import unittest
import random
import word_generator as wg

class WordsTestCase(unittest.TestCase):
    """testing word generator"""

    def setUp(self):
        random.seed()
        self.no_of_tests = 100
        self.min_word_length = 3
        self.max_word_length = 20
        self.min_no_of_words = 15
        self.max_no_of_words = 50

    def test_vowel_consonant(self):
        """check if vowels and consonants are properly interlaced with each other"""
        
        # verify by creating and checking no_of_tests words
        for x in range(self.no_of_tests):
            exemplary_word_length = random.randint(self.min_word_length, self.max_word_length)
            exemplary_word = wg.generate_word(exemplary_word_length)
            for char_index in range(1, len(exemplary_word)):
                # check whether current_char is the opposite type of previous letter
                current_char = exemplary_word[char_index]
                what_type_char_should_be = wg.vowel if (exemplary_word[char_index-1] in wg.consonant) \
                    else wg.consonant
                self.assertIn(current_char, what_type_char_should_be)
            
    def test_length(self):
        """test if generated words are proper length"""
        for x in range(self.no_of_tests):
            exemplary_word_length = random.randint(self.min_word_length, self.max_word_length)
            exemplary_word = wg.generate_word(exemplary_word_length)
            self.assertEqual(len(exemplary_word), exemplary_word_length)

    def test_word_list_length(self):
        """test whether created lists have proper number of elements"""

        for x in range(self.no_of_tests):
            exemplary_list_length = random.randint(self.min_no_of_words, self.max_no_of_words)
            exemplary_list = wg.generate_word_list(exemplary_list_length, \
                self.min_word_length, self.max_word_length)
            self.assertEqual(exemplary_list_length, len(exemplary_list))

unittest.main()