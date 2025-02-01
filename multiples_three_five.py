def solution(number):
    #if the number is negative, return 0
    if number < 0:
        return 0
    
    #use a generator expression to sum numbers below number
    # that are multiples of 3 or 5

    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

# we first check if number is negative.
# we then use a generator expression within sum(). this expression iterates
# over every number from 0 up to (but not including) number
# and checks if it's divisible by 3 or 5 using the modulo operator (%)
# because the condition uses or, if a number is a multiple of both 3 and 5
# it's only added once to the sum.

