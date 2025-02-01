# instead of sum last two, we sum last three.

def tribonacci(signature, n):
    # handle base cases
    if n == 0:
        return []
    if n <= 3:
        return signature[:n]
    # start with given signature/creates copy of signature, prevents modifying original list
    trib_seq = signature[:]

    #generate sequence until it reaches length n
    while len(trib_seq) < n: # checks how many numbers are in the list
        trib_seq.append(sum(trib_seq[-3:])) # sum last 3 elements and append to sequence
    return trib_seq

# we could also use list comprehension to generate the sequence.

def tribonacci(signature, n):
    trib_seq = signature[:n] #take only n elements if n < 3
    [trib_seq.append(sum(trib_seq[-3:])) for _ in range(n - 3)]
    return trib_seq
# a loop inside a list comprehension
# less readable, but more concise.

#slicing allows us to grab the lsat 3 elements dynamically.
# sum is used to calculate the next number in the sequence.
# appending extends the sequence until we reach n elements.
