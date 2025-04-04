def get_book_text (file_path):
    with open(file_path,) as f:
        text = f.read()
    return text

def main():
    file_path = 'books/frankenstein.txt'
    book_text = get_book_text(file_path)

    print(book_text)

main()