import sys
import search



def match_number_to_structure(target_digits,structure, padding,results_so_far=[]):
    #print(padding+"Enter match structure")
    wordlist=[]
    if len(structure)>0:
        wordlist=structure.pop(0) #so we have the words for this itteration and have prepared structure
    else:
        return
    for i in reversed(range(len(target_digits))):
        #print(padding+"We seek a match for the {} digits:{}".format(i+1,target_digits[:i+1]))
        words_found=get_exact_matches_for_number(target_digits[:i+1],wordlist)
        if (words_found):
            results_so_far.append(words_found)
            #print(padding+"We found the following matches:")
            #for word in words_found:
            #    print(padding+word) 
            if (target_digits[i+1:]==""):
                #print(padding+"Whole target matched")
                #Then recusion finnishes, we are done with this branch 
                search.print_results_table(results_so_far)    
                structure.insert(0,wordlist) #because it's recusive.
                results_so_far.pop() 
                return 
            else:
                #print(padding+"Now we need to match the renaming section: {}".format(target_digits[i+1:]))
                match_number_to_structure(target_digits[i+1:],structure, padding+"  ", results_so_far) 
                
                results_so_far.pop() 
                #Don't return here, because the loop will want more
        else:
            print(padding+"We found NO matches")
    structure.insert(0,wordlist) #because it's recusive. 
    return 







def get_exact_matches_for_number(target, words):
    if isinstance(words, list):
            words_found=[]
            for word,number in words.items():
                if (number == target):
                    words_found.append(word) 
            return words_found
    elif isinstance(words, str): 
        word=words
        if (number == target): 
            return [word]
        else:
            return []

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
            updated_structure.append(element)
    
    return updated_structure

        
def find(target,structure): 
  return  match_number_to_structure(target,structure, "",[])
    



if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <digits> <max_matches>")
        sys.exit(1)

    target_digits = sys.argv[1].replace('.','')
    max_matches = int(sys.argv[2])


    structure="ADJECTIVES NOUNS" 
    # Okay, so what we do with structure is: convert everything that isn't a class (NOUNS, VERBS) into a number, and then split the target into the relative bits. 
    # No, we have to split it into a list.  And the wordclasses can be lists of lists, that's NOT a problem for the python. 

    structure=[adjectives,nouns]
    match_number_to_structure(target_digits,structure, "") 

    logger.warning("hello")
