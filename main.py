def get_book_text(file):
    with open(file, "r") as file:
        file_content = file.read()
        return file_content
def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)
main()