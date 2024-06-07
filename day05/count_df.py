import sys
from df_dict import process_file_contents

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py FILENAME")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        characters, lines, words = process_file_contents(filename)
        print(f"Number of characters: {characters}")
        print(f"Number of lines: {lines}")
        print(f"Number of words: {words}")
    except IOError as e:
        print(e)
        sys.exit(1)
