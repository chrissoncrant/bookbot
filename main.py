test_obj = {
    "string_1": "'Shall', 'ascend', 'my', 'funeral', 'pile', 'triumphantly', 'and', 'exult', 'in', 'tHe', 'agony', 'of', 'the', 'torturing', 'flames.', 'The', 'light'",

    "list_1": ['shall', 'ascend', 'my', 'funeral', 'pile', 'triumphantly', 'and', 'exult', 'in', 'the', 'agony', 'of', 'the', 'torturing', 'flames.', 'The', 'light'],

    "obj_1": {"a": 5, "h": 6}
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

def sort_list(dict, rev):
    list = dict_to_list(dict)
    list.sort(key=sort_on, reverse=rev)
    return list

def print_report(word_count, character_list, sort=True):  
    
    if sort:
        sorted = sort_list(character_list, sort)
        character_list = sorted
    header = f"\n---Begin report of book---\n\n{word_count} words found in the document\n\n"
    footer = "---End report---"
    body = ""
    for char in character_list:
        if type(char) == dict:
            key = [key for key in char][0]
            count = char[key]
        else:
            key = char
            count = character_list[char]
        if key == "\n":
            key = "new line"
        new_line = f"The '{key}' character was found {count} time\n"
        body += new_line
    return f"{header}{body}\n{footer}\n"



def main():
    text = get_book_text("./books/frankenstein.txt")

    words = word_count(text)

    character_dictionary = count_characters(text)

    report = print_report(words, character_dictionary, True)

    print(report)

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

# def test(obj):
#     print(obj)
#     for char in obj:
#         if type(char) == dict:
#             key = [key for key in char][0]
#             print("Key: ", key)
#             count = char[key]
#         else:
#             key = char
#             print("Key: ", key)
#             count = obj[char]
#         print(count)
        
# test(test_obj['obj_1'])
# test(c)