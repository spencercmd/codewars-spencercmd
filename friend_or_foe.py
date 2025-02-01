def friend(names):
    # use list comprehension to filter out names that have exactly 4 characters
    # for each name in 'names', check if the length of the name is 4.
    return [name for name in names if len(name) == 4]

