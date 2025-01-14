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

def dict_to_list(dict):
    list = []
    for key in dict:
        list.append({key: dict[key]})
    return list

def sort_on(dict):
    key = [key for key in dict][0]
    return dict[key]

def print_report(word_count, character_list, sort=True):  
    if sort:
        character_list.sort(key=sort_on, reverse=True)
    header = f"\n---Begin report of book---\n\n{word_count} words found in the document\n\n"
    footer = "---End report---"
    body = ""
    for char in character_list:
        key = [key for key in char][0]
        count = char[key]
        new_line = f"The '{key} character was found {count} time\n"
        body += new_line
    return f"{header}{body}\n{footer}\n"



def main():
    text = get_book_text("./books/frankenstein.txt")

    words = word_count(text)

    character_dictionary = count_characters(text)

    print(character_dictionary)

main()

####################
# TEST
####################
# char_count = count_characters(test_obj["string_1"], False)
# c = dict_to_list(char_count)
# # print(c)
# c.sort(key=sort_on, reverse=True)
# # print(c)
# print(print_report(45, c))