from stats import number_of_words, number_of_chars, sort_dict
import sys
def get_book_text(file):
    with open(file, "r") as file:
        file_content = file.read()
        return file_content
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    char_dic = sort_dict(number_of_chars(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {number_of_words(book_text)} total words")
    print("--------- Character Count -------")
    for i in char_dic:
        if i["char"].isalpha() == True:
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
main()