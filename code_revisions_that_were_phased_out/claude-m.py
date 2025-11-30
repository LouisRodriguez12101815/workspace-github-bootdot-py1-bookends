def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)


main()
