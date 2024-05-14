import sys

def count_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            characters = len(contents)
            lines = contents.count('\n') + 1
            words = len(contents.split())

        return characters, lines, words
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python count.py FILENAME")
        sys.exit(1)
    
    filename = sys.argv[1]
    characters, lines, words = count_file_contents(filename)
    print(f"Number of characters: {characters}")
    print(f"Number of lines: {lines}")
    print(f"Number of words: {words}")
