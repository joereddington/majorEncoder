import unittest
from set_generator import convert_to_integer

class TestConvertToInteger(unittest.TestCase):
    def test_valid_word(self):
        # Test a valid word with replacements
        word = "hello"
        result = convert_to_integer(word)
        self.assertEqual(result, "11")

    def test_empty_word(self):
        # Test an empty word
        word = ""
        result = convert_to_integer(word)
        self.assertEqual(result, "")

    def test_word_with_no_replacements(self):
        # Test a word with NO replacements
        word = "aaaeeie"
        result = convert_to_integer(word)
        self.assertEqual(result, "")

    def test_word_with_mixed_replacements(self):
        # Test that all spare letters are removed
        word = "greetings"
        result = convert_to_integer(word)
        self.assertEqual(result, "947290")

    def test_word_with_consecutive_replacements(self):
        # Test a word with consecutive replacements
        word = "change"
        result = convert_to_integer(word)
        self.assertEqual(result, "829")

    def test_word_with_spaces(self):
        # Test a word with spaces (should be replaced)
        word = "hello world"
        result = convert_to_integer(word)
        self.assertEqual(result, "11419")

    def test_word_with_capital_letters(self):
        # Test a word with capital letters 
        word = "Replace"
        result = convert_to_integer(word)
        self.assertEqual(result, "461")

if __name__ == '__main__':
    unittest.main()

