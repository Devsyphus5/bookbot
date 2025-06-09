def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_char_count(book_text):
    book_text = book_text.lower()
    char_counts = {}

    for char in book_text:
        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts

def format_sorted_char_counts(char_counts):
    # Filter only alphabetical characters and create a list of dictionaries
    sorted_list = [{"char": char, "num": count} 
                   for char, count in char_counts.items() if char.isalpha()]
    
    # Sort the list by count in descending order
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    
    return sorted_list

