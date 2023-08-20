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

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <digits> <max_matches>")
        sys.exit(1)

    target_digits = sys.argv[1]
    max_matches = int(sys.argv[2])
    words = load_numbered_words("numbered_words.txt")

    counter = 0
    for combination in find_word_combbinations(target_digits, words):
        print(", ".join(combination))
        counter += 1
        if counter == max_matches:
            break

