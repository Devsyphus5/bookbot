import sys

def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"
    
from stats import get_num_words
from stats import get_char_count
from stats import format_sorted_char_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    
    if book_text.startswith("Error:"):
        print(book_text)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        
        num_words = get_num_words(book_text)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        
        char_counts = get_char_count(book_text)
        formatted_char_counts = format_sorted_char_counts(char_counts)
        
        print("--------- Character Count -------")
        for item in formatted_char_counts:
            print(f"{item['char']}: {item['num']}")
            
        print("============= END ===============")
        
if __name__ == "__main__":
    main()

