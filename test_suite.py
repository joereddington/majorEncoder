import unittest
import io
import sys
from contextlib import redirect_stdout
from search import load_numbered_words, find_word_combinations, get_exact_matches_for_number, print_results_table, match_number_to_structure
import search
import markov
import set_generator

class TestSuite(unittest.TestCase):
    def setUp(self):
        # Initialize any setup required for your tests
        pass

    def test_load_numbered_words(self):
        # Test the load_numbered_words function
        filename = "test_numbered_words.txt"
        with open(filename, 'w') as f:
            f.write("apple: one\nbanana: two\ncherry: three\n")
        
        words = load_numbered_words(filename)
        self.assertEqual(words, {'apple': 'one', 'banana': 'two', 'cherry': 'three'})
    
    def test_find_word_combinations(self):
        # Test the find_word_combinations function
        words = {'apple': '1', 'banana': '2', 'cherry': '3'}
        target = '321'
        combinations = list(find_word_combinations(target, words))
        self.assertEqual(combinations, [['cherry', 'banana', 'apple']])
    
    def test_get_exact_matches_for_number(self):
        # Test the get_exact_matches_for_number function
        words = {'apple': 'one', 'banana': 'two', 'cherry': 'two'}
        matches = get_exact_matches_for_number('two', words)
        self.assertEqual(matches, ['banana', 'cherry'])
    

    def test_markov(self):
        print("Starting test")
        training_string="big dog helped big cat helped"
        model=markov.MarkovChain()
        model.train(training_string)
        print(model.lookup_dict)
        for key in model.lookup_dict:
            print(f"X{key}X")
        target = set_generator.convert_to_integer("helped big dog") # Because we're about to give them 'cat' for free
        combinations = list(search.find_markov_word_combinations(target, model,["cat"]))
        for combination in combinations:
            print(combination)
        print("End of Test")
        
    
    
    def tearDown(self):
        # Clean up any resources created during the tests
        pass

if __name__ == '__main__':
    unittest.main()

