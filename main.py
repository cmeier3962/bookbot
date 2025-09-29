import sys
from stats import word_count, char_count

def get_book_text(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_dict = char_count(text)
    items = list(char_dict.items())
    items.sort(key=lambda pair: pair[1], reverse=True)
    for ch, n in items:
        if ch.isalpha():
            print(f"{ch}: {n}")
        else:
            continue
    print("============= END ===============")

main()