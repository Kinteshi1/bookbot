
def get_word_count(text):
    count = 0
    for word in text.split():
        count += 1
    return count

def get_characters (text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts