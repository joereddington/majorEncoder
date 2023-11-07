import search 
import sys

def recursive_number_combinations(target, unique_numbers,max_results=0):
    all_results=[]
    for number in unique_numbers:
        index = target.find(number)
        if index != -1:
            target_before=target[:index] 
            results_before=[]
            if len(target_before)>0: 
                results_before=recursive_number_combinations(target_before,unique_numbers)
                if len(results_before)==0:
                    return []
            target_after=target[index+len(number):]
            results_after=[]
            if len(target_after)>0: 
                results_after=recursive_number_combinations(target_after,unique_numbers)
                if len(results_after)==0:
                    return []
            to_return = results_before + [number] + results_after
            if max_results==0:
                return(to_return)
            if to_return not in all_results:
                all_results.append(to_return) 
            if len(all_results)>max_results:
                return(all_results)
    return [] 



def find_number_combinations(target, unique_numbers, current=[]):
    if not target:  # if the target string is empty, a solution has been found
        yield current
        #TODO print the range of numbers
        return

    for number in unique_numbers:
        if target.startswith(number):
            # The word can be used. Continue with the remaining target.
            yield from find_number_combinations(target[len(number):], unique_numbers, current + [number])




def find_word_combinations(target, words, current=[]):
    if not target:  # if the target string is empty, a solution has been found
        yield current
        return

    for word, number in words.items():
        if target.startswith(number):
            # The word can be used. Continue with the remaining target.
            yield from find_word_combinations(target[len(number):], words, current + [word])


def brute_force_find(target, matches_to_return):
    words = search.load_numbered_words("numbered_words.txt")
    counter = 0
    for combination in find_word_combinations(target_digits, words):
        print(", ".join(combination))
        counter += 1
        if counter == max_matches:
            break


def print_table_for_number_combination(combination,words):
        columns=[]
        for found_number in combination: 
            #For each number we'll find the words that match.  
            matches=[]
            for word, number in words.items():
                if found_number==number:
                   matches.append(word) 
            #Then we'll put it into a little thing 
            columns.append(matches)
        #Then we print the thing
        search.print_results_table(columns)


def brute_force_number_find(target, matches_to_return):
    words = search.load_numbered_words("numbered_words.txt")
    counter = 0
    unique_numbers = set()

    # Collect the unique numbers from the dictionary
    for word, number in words.items():
        unique_numbers.add(number)
    sorted_unique_numbers = sorted(unique_numbers, key=lambda x: len(str(x)),reverse=True)
    existing=[]
    for combination in find_number_combinations(target_digits, sorted_unique_numbers,existing):
        columns=[]
        for found_number in combination: 
            #For each number we'll find the words that match.  
            matches=[]
            for word, number in words.items():
                if found_number==number:
                   matches.append(word) 
            #Then we'll put it into a little thing 
            columns.append(matches)
        #Then we print the thing
        search.print_results_table(columns)
        
        #TODO - work to do here
        print(", ".join(combination))
        counter += 1
        if counter == max_matches:
            break

def brute_force_biggest(target, matches_to_return):
    words = search.load_numbered_words("numbered_words.txt")
    results=[] 
    for word, number in words.items():
        if number in target:
            if len(number)>2:
                print(f"{number}: {word}") 

def brute_force_anywhere(target,max_matches): 
    words = search.load_numbered_words("big_words.txt")
    counter = 0
    unique_numbers = set()
    # Collect the unique numbers from the dictionary
    for word, number in words.items():
        unique_numbers.add(number)
    sorted_unique_numbers = sorted(unique_numbers, key=lambda x: len(str(x)),reverse=True)
    results= recursive_number_combinations(target,sorted_unique_numbers,max_matches)
    for result in results:
        print(result)
        print_table_for_number_combination(result,words)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <digits> <max_matches>")
        sys.exit(1)

    target_digits = sys.argv[1].replace('.','')
    max_matches = int(sys.argv[2])
#    brute_force_number_find(target_digits,max_matches)
#    brute_force_biggest(target_digits,max_matches)
    brute_force_anywhere(target_digits,max_matches)


# TODO 
# Read words from files like Markov 
# (or at least read a much better numbers file) 
# Combine the results like structure 
