from stats import get_word_count, get_char_count, dict_to_sorted_list

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_content = get_book_text(file_path)

    word_count = get_word_count(book_content)

    char_count = get_char_count(book_content)
    char_count = dict_to_sorted_list(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in char_count:
        for k, v in d.items():
            if k.isalpha():
                print(f"{k}: {v}")
    print("============= END ===============")

main()