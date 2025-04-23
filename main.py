# Import your functions
from stats import count_words, count_chars, sort_char_count
import sys

if len(sys.argv) != 2: 
    print("Usage: python3 main.py <path_to_book>")
    #Exits the code with a system error code 1
    sys.exit(1)
def main():
    #Sets path to the second argument in sys.argv
    path = sys.argv[1]

    # Read the book file
    with open(path) as f:
        file_contents = f.read()

    # Get the word count
    word_count = count_words(file_contents)

    # Get the character count dictionary
    char_count = count_chars(file_contents)

    # Then wherever you need to generate the sorted list
    # Assuming char_count is your dictionary of characters and their counts
    chars_sorted = sort_char_count(char_count)

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # Print each character and its count
    for char_dict in chars_sorted:
        char = char_dict["char"]
        # Skip non-alphabetical characters
        if char.isalpha():
            count = char_dict["num"]
            print(f"{char}: {count}")

    print("============= END ===============")

# Don't forget to call main when the file is run directly
if __name__ == "__main__":
    main()