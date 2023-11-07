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

    def test_find(self):
        noun = search.load_numbered_words("numbered_nouns.txt")
        target = set_generator.convert_to_integer("dog") 
        structure=algorithm_structure.parse_structure("NOUN")
        self.assertEqual(structure[0]['yore'],"4")
        found=False
        for result in algorithm_structure.find(target,structure):
            if "dog" in result:
                found=True
                break
        self.assertTrue(found,"Dog NOT found in results")
        
    
    def test_parse_structure_with_text(self):
        noun = search.load_numbered_words("numbered_nouns.txt")
        structure_text="dog NOUN" 
        target = set_generator.convert_to_integer("dog dog") 
        structure=algorithm_structure.parse_structure(structure_text)
        self.assertEqual(structure[1]['yore'],"4")
        self.assertEqual(structure[0]['dog'],"99")
        results=algorithm_structure.find(target,structure)
        for result in algorithm_structure.find(target,structure):
            if "dog" in result:
                found=True
                break

    def test_parse_structure_with_text(self):
        noun = search.load_numbered_words("numbered_nouns.txt")
        structure_text="The NOUN of  NOUN" 
        target = set_generator.convert_to_integer("The river of blood") 
        structure=algorithm_structure.parse_structure(structure_text)
        results=algorithm_structure.find(target,structure)
        for result in algorithm_structure.find(target,structure):
            print(result)

    def tearDown(self):
        # Clean up any resources created during the tests
        pass

if __name__ == '__main__':
    unittest.main()

