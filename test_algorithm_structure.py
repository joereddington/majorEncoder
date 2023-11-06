import unittest
import io
import sys
import search
import algorithm_structure
import set_generator

class TestSuite(unittest.TestCase):
    def setUp(self):
        # Initialize any setup required for your tests
        pass

    def test_parse_structure(self):
        noun = search.load_numbered_words("numbered_nouns.txt")
        structure_text="NOUN" 
        target = set_generator.convert_to_integer("dog") 
        structure=algorithm_structure.parse_structure(structure_text)
        self.assertEqual(structure[0]['yore'],"4")
        results=algorithm_structure.find(target,structure)
        print("XXX")
        print(results)
        print("XXX")
        self.assertIn("dog",results) 
    
    def test_parse_structure_with_text(self):
        noun = search.load_numbered_words("numbered_nouns.txt")
        structure_text="dog NOUN" 
        target = set_generator.convert_to_integer("dog dog") 
        structure=algorithm_structure.parse_structure(structure_text)
        self.assertEqual(structure[0]['yore'],"4")
        results=algorithm_structure.find(target,structure)
        self.assertIn("dog",results) 


    def tearDown(self):
        # Clean up any resources created during the tests
        pass

if __name__ == '__main__':
    unittest.main()

