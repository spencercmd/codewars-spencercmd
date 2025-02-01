def alphabet_position(text):
    result = []
    # loop over each character in the input text.
    for char in text:
        # check if the character is an alphabet letter
        if char.isalpha():
            # convert to lowercase
            # calculate its position in the alphabet
            # ord('a') is 97, so subtracting 96 gives us the position in the alphabet.
            position = ord(char.lower()) - 96
            result.append(str(position))

    # join the positions with spaces and return the result.
    return ' '.join(result)

# order is based on ascii tables/values.
# ord() returns the ascii value of the character.
# char.lower() ensures that we're always working with lowercase letters.
# subtracting 96 from the ascii value gives us the position in the alphabet.
# we then convert the position to a string and append it to the result list.

