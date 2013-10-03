# Multiply all the elements in a list
def multiply(l):
    if l == []:
        return 1
    return l[0] * multiply(l[1:])

# Compute factorial of a number    
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
    
# Count the number of elements in the list l
def count_list(l):
    if l == []:
        return 0
    return 1 + count_list(l[1:])

# Sum all of the elements in a list
def sum_list(l):
    if l == []:
        return 0
    return l[0] + sum_list(l[1:])

# Reverse a list without slicing or loops
def reverse(l):
    if l == []:
        return [] 
    n = l.pop()
    return [n] + reverse(l)

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l == []:
        return False
    if l[0] == i:
        return True
    return find(l[1:], i) 

# Determines if a string is a palindrome
def palindrome(some_string):
    if len(some_string) <= 1:
        return True
    elif some_string[0] != some_string[-1]:
        return False
    return palindrome(some_string[1:-1])

# Given the width and height of a sheet of paper, and the number of times to fold it, 
# return the final dimensions of the sheet as a tuple. Assume that you always fold in 
# half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0 or width == 0 or height == 0:
        return (width, height)
    else:
        if width >= height:
            return fold_paper(width/2., height, folds - 1)
        else: 
            return fold_paper(width, height/2., folds - 1)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    if n == target:
        print target
    elif n < target:
        print n 
        count_up(target, n + 1)


n = range(1,6)
# print multiply(n)
# print count_list(n)
# print sum_list(n)
# print reverse(n)
# print factorial(5)
# print fibonacci(15)
# print find(n, 5)
# print palindrome("bba")
# count_up(10, 0)
# print fold_paper(1,18,10)