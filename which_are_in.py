def in_array(a1, a2):
    # use a set to avoid duplicates and store words from a1 that are found in a2
    result = {word for word in a1 if any(word in s for s in a2)}
    # return sorted list of results
    return sorted(result)

# set comprehension:
# word in s checks if word from a1 exists inside any string s from a2
# any(...) ensures we check every word in a2
# Set {} removes any duplicates automatically

# Sorting we return the found words in lexicographical order (dictionary order)
