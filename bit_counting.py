def count_bits(n):
    # convert n to a binary string
    # count and return number of 1s in binary string

    return bin(n).count('1')

# bin() converts n to a binary string.
# .count('1') counts the number of 1s in the binary string.
# we could also try Brian Kernighan's algorithm to count the number of 1s in the binary string.

def count_bits(n):
    count = 0
    while n:
        # n - 1 flips all the bits after the rightmost set bit (including the rightmost set bit)
        n &= n -1
        count += 1
    return count

# Brian Kernighan's algorithm is more efficient for this problem.
# it works by flipping the rightmost set bit and all the bits after it to 0.
# this is equivalent to counting the number of 1s in the binary string.