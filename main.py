import sys
from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    num_chars = get_num_chars(text)
    # print(num_chars)
    sorted_dict_list = get_sorted(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {sys.argv[1]}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for item in sorted_dict_list:
        print(f"{item['char']}: {item['num']}")

    # OOT.DEV Solution
    # for item in chars_sorted_list:
    #     if not item["char"].isalpha():
    #         continue
    #     print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
