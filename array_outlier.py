def find_outlier(integers):
    # Check the first three numbers to decide the majority parity.
    first_three = integers[:3]
    even_count = sum(1 for num in first_three if num % 2 == 0)
    
    # If at least two are even, then even is the majority.
    majority_even = even_count >= 2
    
    # Now, find the number that doesn't match the majority.
    for num in integers:
        if majority_even:
            if num % 2 != 0:
                return num
        else:
            if num % 2 == 0:
                return num
