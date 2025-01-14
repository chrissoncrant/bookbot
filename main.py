test_obj = {
    "string_1": "'shall', 'ascend', 'my', 'funeral', 'pile', 'triumphantly', 'and', 'exult', 'in', 'the', 'agony', 'of', 'the', 'torturing', 'flames.', 'The', 'light'",
    "list_1": ['shall', 'ascend', 'my', 'funeral', 'pile', 'triumphantly', 'and', 'exult', 'in', 'the', 'agony', 'of', 'the', 'torturing', 'flames.', 'The', 'light']
}

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def count_characters(string, character):
    lowercase_string = string.lower()
    character_dictionary = {}
    for char in character:
        char = char.lower()
        character_dictionary[char] = lowercase_string.count(char)
    
    return character_dictionary

print(count_characters(test_obj["string_1"], test_obj["list_1"]))
def main():
    text = get_book_text("./books/frankenstein.txt")

    words = word_count(text)

    print(f"{words} words in this text.")



# main()