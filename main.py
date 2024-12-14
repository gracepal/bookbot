
def main():
    book_path = "./books/frankenstein.txt"
    book_content = read_book(book_path)
    num_words = count_words(book_content)
    num_chars = count_chars(book_content)

    # print a report
    print(f"--- Begin report of {book_path.lstrip('./')} ---")
    print(f"{num_words} words found in the document\n")
    for ch, count in num_chars.items():
        print(f"The '{ch}' character was found {count} times")
    print("\n--- End report ---")

def read_book(book_path):
    with open(book_path, 'r') as fp:
        content = fp.read()
    return content

def count_words(s):
    return len(s.split())

def count_chars(s):
    chars = {}
    for ch in s:
        if ch.isalpha():
            key = ch.lower()
            chars[key] = 1 + chars.get(key, 0)
    return chars


main()