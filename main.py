from stats import number_of_words
def get_book_text(file):
    with open(file, "r") as file:
        file_content = file.read()
        return file_content
def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {number_of_words(book_text)} total words")
main()