def duplicate_encode(word):
    #convert the string to lowercase to ignore capitalization differences
    word_lower = word.lower()

    # create a dictionary to count how many times each character appears

    frequency = {}
    for char in word_lower:
        frequency[char] = frequency.get(char, 0) + 1

        # build the encoded string 
    encoded = ""
    for char in word_lower: 
        if frequency[char] == 1:
            encoded += "("
        else:
            encoded += ")"

    return encoded

# we first convert the input to lowercase (word.lower()) so that chars like "S" and "s" are treated the same
# we iterate over each character and use a dict (frequency) to count how many times
# each one appears.
# for every character in the lowercase word, we append "(" if its frequency is 1; otherwise
# we appened ")"
