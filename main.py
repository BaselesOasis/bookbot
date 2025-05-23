import sys

from stats import get_word_count
from stats import get_char_count

def get_book_txt(relativ_book_path):
    with open(relativ_book_path) as book:
        book_txt = book.read()
    return book_txt

def sort_char_dict(char_dict):
    sorted_char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse = True))
    return sorted_char_dict


def main():
    if len(sys.argv) > 1:
        relativ_book_path = sys.argv[1]
        try:

            book_txt = get_book_txt(relativ_book_path)
            num_words = get_word_count(book_txt)
            char_dict = get_char_count(book_txt)
            sorted_char_dict = sort_char_dict(char_dict)

            print("============ BOOKBOT ============")
            print("Analyzing book found at books/frankenstein.txt...")
            print("----------- Word Count ----------")
            print(f"Found {num_words} total words")
            print("--------- Character Count -------")
            for key in sorted_char_dict:
                print(f"{key}: {sorted_char_dict[key]}")
            print("============= END ===============")
        except FileNotFoundError:
            print(f"Error: no file found in {relativ_book_path}")
        except Exception as e:
            print("Error: unexpected error occoured: {e}")

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    
main()
    
        