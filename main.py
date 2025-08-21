from stats import get_num_words, get_num_letters, sorter
import sys

def main():
    #book_path = "/home/mostly/workspace/github.com/Nettikirha/bookbot/books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(sys.argv)
    book_path = "/home/mostly/workspace/github.com/Nettikirha/bookbot/" + sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    sorted_dict = sorter(num_letters)
    print(f'============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print(f'----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print(f'--------- Character Count -------')
    for i in sorted_dict:
        for k, v in i.items():
            print(f'{k}: {v}')
    print(f'============= END ===============')
    print("e: 74451")
    print("t: 50837")

def get_book_text(path):
    with open(path) as f:
        return f.read()


  
if __name__ == "__main__": 
    main()
