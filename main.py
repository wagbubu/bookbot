def main():
    report_character_count("./books/frankenstein.txt")

def get_num_words(text):
    words = text.split(" ")
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_character_count(text):
    char_count_dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char not in char_count_dict:
            char_count_dict[lowered_char] = 1
        else:
            char_count_dict[lowered_char] += 1
    return char_count_dict

def char_count_dict_to_list(char_count_dict):
    char_dict_list = list()
    for char in char_count_dict:
        ascii_val = ord(char) 
        if ascii_val > 96 and ascii_val < 123:
            single_char_count = dict()
            single_char_count["letter"] = char
            single_char_count["count"] = char_count_dict[char]
            char_dict_list.append(single_char_count)
    return char_dict_list

def report_character_count(book_path):
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_count_dict = get_character_count(text)
    char_count_list = char_count_dict_to_list(char_count_dict)
    #sort list
    char_count_list.sort(key=lambda dict: dict["count"], reverse=True)


    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for single_char_dict in char_count_list:
        print("The " + single_char_dict["letter"] + " character was found " + str(single_char_dict["count"]) + " times")  
    print("--- End report ---")

main()