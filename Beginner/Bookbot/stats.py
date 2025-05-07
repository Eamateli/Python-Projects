def get_num_words(text):
    return len(text.split())

def get_num_character(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_num_character_sorted(charactes_dictionary):
    new_char_count = []
    for char, count in charactes_dictionary.items():
        if char.isalpha():
            char_info = {char:count}
            new_char_count.append(char_info)
        
    new_char_count.sort(reverse=True, key=lambda d: list(d.values())[0])
    return new_char_count

