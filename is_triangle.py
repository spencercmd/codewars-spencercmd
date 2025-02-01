def is_triangle(a, b, c):
    # each side must be greater than zero (cant build with rope of negative/zero length)
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # next, check the triangle inequality theorem
    # sum of any two sides must be greater than the third side
    # ensures real triangle can be formed

    if a + b <= c or a + c <= b or b +c <= a:
        return False
    # if both conditions are satisfied, it is a triangle

    return True

# after reviewing other solutions, I believe that the first constraint is not necessary.
# the triangle inequality theorem is sufficient to determine if a triangle can be formed, as a negative value would not form a triangle.
