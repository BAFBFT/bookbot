from stats import count_words, count_characters, sort_dict, print_report
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Error - Correct Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #extract text
    book = get_book_text(sys.argv[1])
    
    #count the num of words
    num_words = count_words(book)
    print("{:d} words found in the document".format(num_words))
    
    #count the num of characters and group them
    characters_list = sort_dict(count_characters(book))

    print_report(characters_list, sys.argv[1], num_words)

    return

if __name__ == "__main__":
    main()



