def iterative_factorial(n):
    # positive numbers only
    fact = 1 
    for i in range(2, n + 1):
        fact *= i
    return fact
# print(iterative_factorial(5))

# Recursive approach
def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n-1)
        temp = temp * n
        print(temp)
    return temp
# our last number in becomes our first number out 
print(recur_factorial(5))

# in this particular case, recursion takes more space and time by running 
# back to the function call to create those pockets for our numbers versus
# iteration where it's simply multiplying each number in place and not 
# creating anything new. 