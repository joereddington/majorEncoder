import sys
def convert_to_integer(word):
    replace_dict = {
        'l': '1',
        'n': '2',
        'm': '3',
        'r': '4',
        'f': '5',
        'v': '5',
        'b': '6',
        'p': '6',
        't': '7',
        'ch': '8',
        'sh': '8',
        'g': '9',
        's': '0',
        'd': '9',
        'z': '0'
    }

    # Reverse the replace_dict for easier replacement
    replace_dict_reverse = {k: v for k, v in replace_dict.items()}

    for key, value in replace_dict_reverse.items():
        word = word.replace(key, value)
    # Remove all non-numeric characters
    result = ''.join([char for char in word if char.isdigit()])
    
    return result

def process_file():
    # Open input and output files
    target_file = sys.argv[1]
    with open(target_file, 'r') as infile, open('numbered_'+target_file, 'w') as outfile:
        # Iterate over each line in the input file
        for line in infile:
            word = line.strip()  # Remove newline characters
            converted = convert_to_integer(word)
            
            # Write to the output file
            outfile.write(f"{word}: {converted}\n")

# Execute the function to process the file
#print(convert_to_integer("bail"))
#print(convert_to_integer("skywalker"))

if __name__ == '__main__':
    process_file()

