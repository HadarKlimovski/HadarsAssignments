def count_characters(contents):
    return len(contents)

def count_lines(contents):
    return contents.count('\n') + 1

def count_words(contents):
    return len(contents.split())

def process_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
        characters = count_characters(contents)
        lines = count_lines(contents)
        words = count_words(contents)
        return characters, lines, words
    except Exception as e:
        raise IOError(f"Error processing file: {e}")
