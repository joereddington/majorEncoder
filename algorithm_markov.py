import random
import search
import set_generator
import sys
import string


shortest_chain=9


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

def find_markov_word_combinations(target, model, current=[]):
    global shortest_chain
    if not target:  # if the target string is empty, a solution has been found
        print(f"Found one of length {len(current)} compared to {shortest_chain}: {current}")
        if len(current)<shortest_chain:
            shortest_chain=len(current)
        yield current
        return
    if len(current)>=shortest_chain:
        return #there are shorter versions
    if current: 
        last_word=current[-1]
        words_that_could_follow=model.lookup_dict[last_word]
        for option in words_that_could_follow:
            number=set_generator.convert_to_integer(option)
            if number=="":
                continue
            if target.startswith(number):
                yield from find_markov_word_combinations(target[len(number):], model, current + [option])
    else: 
        sorted_options = sorted(model.lookup_dict, key=key_function, reverse=True)
        for option in sorted_options: #So all the words in the damn file sorted by length
            number=set_generator.convert_to_integer(option) #TODO - doing this twice.
            #TODO sort by length
            if len(number)<1: #Because some words don't have numbers
                continue
            if target.startswith(number):
                yield from find_markov_word_combinations(target[len(number):], model, current + [option])

# Define a key function to calculate the length of converted integers
def key_function(option):
    integer_result = set_generator.convert_to_integer(option)
    return len(integer_result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <digits> <max_matches>")
        sys.exit(1)

    target = sys.argv[1].replace('.','')
    model=MarkovChain()
    test=False
    if test:
        print("Training on the hobbit")
        model.train_from_file("testinputs/hobbit.txt")
    else:
        from pathlib import Path
        directory_path=Path("sources") 
        for file_path in directory_path.iterdir():
            if file_path.is_file():
                print(f"Training on {file_path}")
                model.train_from_file(file_path) 
    print(f"our target is {target}")
    results = list(find_markov_word_combinations(target, model,[]))
    # TODO should print somehting here. 




