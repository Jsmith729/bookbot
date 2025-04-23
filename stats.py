def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_count = {}
    
    for c in text:
        char = c.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_by_count(char_dict):
    return char_dict["num"]

def sort_char_count(char_count_dict):
    # Create a list to hold our dictionaries
    chars_list = []
    
    # Convert each character and count into a dictionary and add to the list
    for char, count in char_count_dict.items():
        chars_list.append({"char": char, "num": count})
    
    # Now we need to sort the list by count (highest to lowest)
    # What sorting function could you use here?
    chars_list.sort(reverse=True, key=sort_by_count)
    return chars_list

