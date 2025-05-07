from stats import get_num_words, get_num_character, get_num_character_sorted

def get_book_text(path):
    with open(path) as f:
        return f.read()



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_character(text)
    sorted_num_chars = get_num_character_sorted(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_num_chars:
        for char, count in item.items(): 
            print(f"{char}: {count}")
    print("============= END ===============")

main()







# def get_book_text():
#     with open("books/frankenstein.txt") as f:
#         return f.read()
    
# def number_of_words():
#     words = get_book_text().split()
#     return len(words)

    
# def main():
#     print(f"{number_of_words()} words found in the document")

# main()
