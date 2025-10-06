from stats import number_of_words, number_of_chars
def get_book_text(file):
    with open(file, "r") as file:
        file_content = file.read()
        return file_content
def main():
    book_text = get_book_text("books/frankenstein.txt")
    char_dic = number_of_chars(book_text)
    print(f"Found {number_of_words(book_text)} total words")
    print(char_dic)
main()