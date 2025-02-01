def digital_root(n):
    # continue to sum the digits of n until a single digit is obtained
    while n >= 10: #as long as n has more than one digit
        n = sum(int(digit) for digit in str(n)) #convert n to a string, iterate over each character, convert each character back to an integer, and sum the integers
    return n

# python integers are not iterable by themselves - you cant directly loop over each digit in a number.
# we can convert the number to a string, iterate over each character, convert each character back to an integer, and sum the integers.




