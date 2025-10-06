def get_book_text(file):
    with open(file, "r") as file:
        file_content = file.read()
        return file_content
def number_of_words(text):
    return len(text.split())
def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {number_of_words(book_text)} total words")
main()