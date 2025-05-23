def get_word_count(book_txt):
    split_txt = book_txt.split()
    word_count = 0
    for word in split_txt:
        word_count += 1
    return word_count

def get_char_count(book_txt):
    lower_text = book_txt.lower()
    char_dict = {}
    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict