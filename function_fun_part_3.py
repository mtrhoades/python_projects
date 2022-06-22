#Please complete the following functions.

# name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.
def name_args(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{kwargs[k]}")

name_args(a="arthur", b="bruce")


# all_true - Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.
# one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.
# recursive_factorial - Uses recursion to find the factorial of an integer.
# recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.
# Input: AABBCCDD
# Output: ABCD
# recursive_reverse - Uses recursion to reverse a string.

