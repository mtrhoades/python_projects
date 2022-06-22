
# arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for arg in args:
        print(arg)

arb_args('dog', 'cat', 'fish', 'lizard')  


# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
def inner_func(a, b):
    def sum(a, b):
        return a + b
    print(sum(a, b))

    def subtract(a, b):
        return a - b
    print(subtract(a, b))

inner_func(5, 5)


#lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(studentName, lunch="Mystery Meat"):
    print(studentName, lunch)

lunch_lady('Matthew', 'Shrimp and Grits')
lunch_lady('Matthew')


#sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(a, b):
    return a+b, a*b

print(sum_n_product(2, 5))


# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
alias_arb_args = arb_args


# # arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*args):
    total = 0
    for a in args:
        total += a
        print(a/len(args))

arb_mean(4, 6, 32, 23, 0)


# # arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*args):
    long = 0
    longest = ''
    for a in args:
        if len(a) > long:
            long = len(a)
            longest = a

    return longest
    
print(arb_longest_string('dog', 'cat', 'fish', 'gecko', 'elephant'))