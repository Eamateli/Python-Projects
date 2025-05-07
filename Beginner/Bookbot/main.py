from stats import get_num_words


def get_book_text(path):
    with open(path) as f:
        return f.read()



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

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
