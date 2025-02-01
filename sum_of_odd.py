# each row n contains n consecutive odd numbers.
# the formula fo the kth odd number is 2k-1
# by working out the arithmetic, you can show that the sum of these n odd numbers in the nth row comes
# neatly to n^3

def row_sum_odd_numbers(n):
    # the sum of the nth row is n^3
    return n**3

# this function directly returns n^3 since thats the sum of the nth row of odd numbers.
# row 1 contains 1 number
# row 2 contains 2 numbers
# row 3 contains 3 numbers
# row n contains n consecutive odd numbers.

# before row n, the total of odd numbers used is the sum of the first (n-1) rows.
# so the first odd number in row n is the last odd number in row (n-1) + 2.
# the last odd number in row n is the first odd number in row (n+1) - 2.