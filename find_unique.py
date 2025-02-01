def find_uniq(arr):
    # determine majority element using first three values
    # if the first two are the same, thats our majority

    if arr[0] == arr[1]:
        majority = arr[0]
    else:
        # otherwise, the first two are different, so we check the third.

        majority = arr[0] if arr[0] == arr[2] else arr[1]

        # now, find and return the element that is not equal to the majority
    for num in arr:
        if num != majority:
            return num

# by comparing the first three elements, we can confidently decide which value appears most frequently
# loop over the array and return the element that does not match the majority. Since there is only one unique element, this loop stops as soon as it finds it.

# we ran into an issue here and failed two tests:
# none should equal 2
# none should equal 0.55
