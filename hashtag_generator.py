def generate_hashtag(s):
    # check if input is empty
    if not s or s.strip() == "":
        return False
# split the input into words, automatically handling extra spaces
    words = s.split()

#capitalize each word and join them together, then prepend a "#"

    hashtag = '#' + ''.join(word.capitalize() for word in words)

    #if the final result is longer than 140 chars, return False
    return hashtag if len(hashtag) <= 140 else False

# input check: condition ensures that if the input is empty or only contains spaces
# we return False.
# s.split() splits the string into words while automatically removing extra spaces.
# generator expression capitalizes the first letter of each word. We then join them together
# and add a '#' at the beginning.

# finally, length check. if the hashtag's length exceeds 140 chars, we return False.

# s.split() treats any sequence of whitespace chars as a new single delimiter. So even if there are multiple
# spaces in a row, they're all considered one split point.

# Leading or trailing spaces are ignored.
