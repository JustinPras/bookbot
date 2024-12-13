def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    num_words = get_number_of_words(book_text)
    chars_dict = get_char_appearances(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_words} words found in the document\n")
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_number_of_words(text):
    return len(text.split())

def get_char_appearances(text):
    lower_text = text.lower()
    chars = {}
    for c in text:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    return chars

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

main()