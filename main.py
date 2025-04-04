from stats import get_word_count
from stats import get_book_text
from stats import get_characters

def main():
    file_path = 'books/frankenstein.txt'
    book_text = get_book_text(file_path)
    word_count = get_word_count(book_text)
    character_count = get_characters(book_text)

    print(f"{word_count} words found in the document")
    print(character_count)


main()