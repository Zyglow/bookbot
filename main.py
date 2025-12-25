from stats import pText, cChars, sortList
import sys

def get_book_text(content):
    with open(content, 'r') as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = sys.argv[1]

    # Currying FTW
    num_words = pText(get_book_text(content))
    charDict = cChars(get_book_text(content))

    # Print Results
    print(f"============ BOOKBOT ============\nAnalyzing book found at {content}...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sortedChars = sortList(charDict)
    for item in sortedChars:
        print(f"{item[0]}: {item[1]}")
    print("============= END ===============")

main()