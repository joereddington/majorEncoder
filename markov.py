import random
import set_generator
import sys
import string

class MarkovChain:
    def __init__(self):
        self.lookup_dict = {}


    def _generate_lookup_dict(self, text):
        # Function to remove non-alphabetic characters from a string
        def remove_non_alphabetic(input_str):
            return ''.join(char for char in input_str if char.isalpha())

        # Use list comprehension to apply the function to each element in the list
        cleaned_text = [remove_non_alphabetic(element) for element in text]

        for i in range(0, len(text) - 1):
            key = cleaned_text[i]
            next_word = cleaned_text[i+1]
            if True: 
                if key in self.lookup_dict:
                    self.lookup_dict[key].add(next_word)
                else:
                    self.lookup_dict[key] = {next_word}
        for key in self.lookup_dict:
            self.lookup_dict[key]=set(sorted(self.lookup_dict[key], key=lambda x: len(x),reverse=True))

    def train(self, text):
        tokens = text.split(' ')
        self._generate_lookup_dict(tokens)

    def train_from_file(self, filename):
        with open(filename, 'r', errors='ignore') as file:
            text = file.read().lower()
            self.train(text)

    def generate_text(self, max_length=100):
        context = random.choice(list(self.lookup_dict.keys()))
        output = list(context)

        for i in range(max_length):
            if context in self.lookup_dict:
                next_word = random.choice(self.lookup_dict[context])
                output.append(next_word)
                context = tuple(output[-len(context):])
            else:
                break

        return ' '.join(output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py path_to_file")
        sys.exit(1)

    filename = sys.argv[1]
    chain = MarkovChain()
    chain.train_from_file(filename, order=2)
    generated_text = chain.generate_text()
    print(generated_text)

