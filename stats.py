def get_book_text (file_path):
    with open(file_path,) as f:
        text = f.read()
    return text

def get_word_count(text):
    count = 0
    for word in text.split():
        count += 1
    return count