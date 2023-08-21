import sys

def load_numbered_words(filename):
    word_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            word, number = line.strip().split(": ")
            word_dict[word] = number
    
    # Sort words by the length of their number, longest first
    sorted_words = dict(sorted(word_dict.items(), key=lambda item: len(item[1]), reverse=True))
    return sorted_words

def find_word_combbinations(target, words, current=[]):
    if not target:  # if the target string is empty, a solution has been found
        yield current
        return

    for word, number in words.items():
        if target.startswith(number):
            # The word can be used. Continue with the remaining target.
            yield from find_word_combbinations(target[len(number):], words, current + [word])


def get_exact_matches_for_number(target, words):
        words_found=[]
        for word,number in words.items():
            if (number == target):
                words_found.append(word) 
        return words_found

def print_results_table(columns):
    if not columns:
        print("Empty table")
        return
    
    print("A result:")
    # Find the maximum number of rows
    max_rows = max(len(column) for column in columns)
    
    # Find the maximum width of each column
    column_widths=[]
    for column in columns: 
        length=len(max(column, key =len))
        column_widths.append(length)
    # Print the table
    for row_index in range(max_rows):
        formatted_row = [str(column[row_index]).ljust(width) if row_index < len(column) else ''.ljust(width) for column, width in zip(columns, column_widths)]
        print(" | ".join(formatted_row))

    
def match_number_to_structure(target_digits,structure, padding,results_so_far=[]):
    #print(padding+"Enter match structure")
    wordlist=structure.pop(0) #so we have the words for this itteration and have prepared structure
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
                print_results_table(results_so_far)    
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


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <digits> <max_matches>")
        sys.exit(1)

    target_digits = sys.argv[1].replace('.','')
    max_matches = int(sys.argv[2])
    words = load_numbered_words("numbered_words.txt")
    verbs = load_numbered_words("numbered_verbs.txt")
    nouns = load_numbered_words("numbered_nouns.txt")
    adjectives = load_numbered_words("numbered_adjectives.txt")


    # New Approach   
    structure=[adjectives,nouns,verbs,nouns]
    match_number_to_structure(target_digits,structure, "") 


    counter = 0
    for combination in find_word_combbinations(target_digits, words):
        print(", ".join(combination))
        counter += 1
        if counter == max_matches:
            break

