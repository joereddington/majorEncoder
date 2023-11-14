import unittest
import io
import sys
from contextlib import redirect_stdout
from search import load_numbered_words, find_word_combinations, get_exact_matches_for_number, print_results_table, match_number_to_structure
import search
import algorithm_markov
import set_generator

class TestSuite(unittest.TestCase):
    def setUp(self):
        # Initialize any setup required for your tests
        pass

    def test_load_numbered_words(self):
        # Test the load_numbered_words function
        filename = "testinputs/test_numbered_words.txt"
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
        training_string="big dog helped big cat helped"
        model=markov.MarkovChain()
        model.train(training_string)
        target = set_generator.convert_to_integer("helped big dog") # Because we're about to give them 'cat' for free
        first_combination = list(search.find_markov_word_combinations(target, model,["cat"]))[0]
        self.assertEqual(first_combination,['cat', 'helped', 'big', 'dog'])
        
    def test_markov_stop(self):
        training_string="big. dog helped big cat helped"
        model=markov.MarkovChain()
        model.train(training_string)
        target = set_generator.convert_to_integer("helped big dog") # Because we're about to give them 'cat' for free
        first_combination = list(search.find_markov_word_combinations(target, model,["cat"]))[0]
        self.assertEqual(first_combination,['cat', 'helped', 'big', 'dog'])


    def test_markov2(self):
        training_string="big dog helped big cat helped"
        model=markov.MarkovChain()
        model.train(training_string)
        target = set_generator.convert_to_integer("cat helped big dog") 
        first_combination = list(search.find_markov_word_combinations(target, model,[]))[0]
        self.assertEqual(first_combination,['cat', 'helped', 'big', 'dog'])
    

    def test_markov_no_doubles(self):
        training_string="apples bears apples pears apples bears"
        model=markov.MarkovChain()
        model.train(training_string)
        self.assertEqual(sorted(model.lookup_dict["apples"]),sorted(["pears","bears"]))

    def test_markov_protonmass(self):
        model=markov.MarkovChain()
        model.train_from_file("testinputs/hobbit.txt")
        from pathlib import Path
        directory_path=Path("sources") 
        for file_path in directory_path.iterdir():
            if file_path.is_file():
                print(file_path)
                model.train_from_file(file_path) 
        target = "167262192369" #proton mass
        first_combination = list(search.find_markov_word_combinations(target, model,[]))[0]
        self.assertEqual(first_combination,['cat', 'helped', 'big', 'dog'])
   

    def test_markov_ordering(self):
        model=markov.MarkovChain()
        training_string="apple bbb apple bb apple bbbb apple b"
        model.train(training_string)
        self.assertEqual(sorted(model.lookup_dict["apple"]),sorted(['bb', 'bbbb', 'bbb', 'b']))

    def test_markov_ordering2(self):
        model=markov.MarkovChain()
        training_string="apple bbb apple baaaab apple bbbb apple b"
        model.train(training_string)
        self.assertEqual(sorted(model.lookup_dict["apple"]),sorted(['baaaab', 'bbbb', 'b', 'bbb']))

    

    def tearDown(self):
        # Clean up any resources created during the tests
        pass

if __name__ == '__main__':
    unittest.main()

