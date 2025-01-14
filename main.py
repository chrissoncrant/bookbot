test_obj = {
    "string_1": "'Shall', 'ascend', 'my', 'funeral', 'pile', 'triumphantly', 'and', 'exult', 'in', 'tHe', 'agony', 'of', 'the', 'torturing', 'flames.', 'The', 'light'",

    "list_1": ['shall', 'ascend', 'my', 'funeral', 'pile', 'triumphantly', 'and', 'exult', 'in', 'the', 'agony', 'of', 'the', 'torturing', 'flames.', 'The', 'light']
}

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def count_characters(text, onlyLetters = True):
    character_dictionary = {}
    def counter(char):
        if char in character_dictionary:
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1  

    for char in text:
        char = char.lower()
        if onlyLetters:
            if char.isalpha():
                counter(char)
        else:
            counter(char)
    
    return character_dictionary



# print(count_characters(test_obj["string_1"], False))
def main():
    text = get_book_text("./books/frankenstein.txt")

    words = word_count(text)

    character_dictionary = count_characters(text)

    print(character_dictionary)



main()