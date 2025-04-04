import sys

from dnf.util import empty

from stats import(
    get_word_count,
    get_characters,
    chars_dict_to_sorted_list,
)

def get_book_text (file_path):
    with open(file_path,) as f:
        text = f.read()
    return text

def main():

    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = get_word_count(book_text)
    characters_count = get_characters(book_text)
    characters_sorted = chars_dict_to_sorted_list(characters_count)


    print("============ BOOKBOT ============")
    print(f"Analyzing Book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for entry in characters_sorted:
        if not entry["char"].isalpha():
            continue
        print(f"{entry["char"]}: {entry["count"]}")
main()