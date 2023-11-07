import sys
import search
import set_generator


def find_word_combinations(target, structure, current=[]):
    if not target:  # if the target string is empty, a solution has been found
        yield current
        return
    wordlist=[]
    if len(structure)>0:
        wordlist=structure.pop(0) #so we have the words for this iteration and have prepared structure
    else:
        return

    for word, number in wordlist.items():
        if target.startswith(number):
            # The word can be used. Continue with the remaining target.
            yield from find_word_combinations(target[len(number):], structure, current + [word])
    structure.insert(0,wordlist) #because it's recursive. 
    return 


def parse_structure(structure): 
    structure_list=structure.split()
    verbs = search.load_numbered_words("numbered_verbs.txt")
    nouns = search.load_numbered_words("numbered_nouns.txt")
    adjectives = search.load_numbered_words("numbered_adjectives.txt")
    updated_structure = []

    # Iterate through each element in the structure list
    for element in structure_list:
        # Check if the element is a placeholder like "NOUN" or "VERB"
        if element == "NOUN":
            # Replace with a random noun from the nouns list or your logic
            updated_structure.append(nouns)
        elif element == "VERB":
            # Replace with a random verb from the verbs list or your logic
            updated_structure.append(verbs)
        elif element == "ADJECTIVE":
            # Replace with a random adjective from the adjectives list or your logic
            updated_structure.append(adjectives)
        else:
            # Keep the original element if it's NOT a placeholder
            word_dict={}
            word_dict[element] = set_generator.convert_to_integer(element)
            updated_structure.append(word_dict)
    
    return updated_structure

        
def find(target,structure): 
  return  find_word_combinations(target,structure,[])
    

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <digits> <max_matches>")
        sys.exit(1)

    target_digits = sys.argv[1].replace('.','')
    max_matches = int(sys.argv[2])
    sentence_structures = [
    "The NOUN of the NOUN VERB.",
    "NOUN VERB the NOUN.",
    "A NOUN can VERB a NOUN.",
    "NOUN VERB when the NOUN is NOUN.",
    "The NOUN is NOUN to VERB.",
    "NOUN is NOUN, but NOUN VERB differently.",
    "NOUN can VERB if NOUN is NOUN.",
    "NOUN VERB the NOUN with NOUN.",
    "When NOUN VERB, the NOUN is NOUN.",
    "NOUN VERB NOUN, and NOUN is NOUN.",
    "NOUN NOUN NOUN NOUN NOUN NOUN NOUN NOUN NOUN NOUN NOUN"
    ]

    #structure_text="The NOUN of  NOUN" 
    for structure_text in sentence_structures:
        print(structure_text)
        structure=parse_structure(structure_text)
        for result in find(target_digits,structure):
            print(result)

