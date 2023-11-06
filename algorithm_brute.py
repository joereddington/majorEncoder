import search 
import sys


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


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <digits> <max_matches>")
        sys.exit(1)

    target_digits = sys.argv[1].replace('.','')
    max_matches = int(sys.argv[2])
    brute_force_find(target_digits,max_matches)


# TODO 
# Read words from files like Markov 
# (or at least read a much better numbers file) 
# Combine the results like structure 
