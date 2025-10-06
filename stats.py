def number_of_words(text):
    return len(text.split())
def number_of_chars(text):
    result = {}
    for char in text:
        char = char.lower()
        if not char in result:
            result[char] = 0
        result[char] += 1
    return result