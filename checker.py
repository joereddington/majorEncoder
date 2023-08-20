import sys
import set_generator

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script_name.py word1 word2 ...")
        sys.exit(1)

    words = sys.argv[1:]
    result_number = ''.join(set_generator.convert_to_integer(word) for word in words)
    
    print(f"Given words: {' '.join(words)}")
    print(f"Generated number: {result_number}")

