def permute(string, pocket=""):
    # first eval if the string is empty
    if len(string) == 0:
        print(pocket)
    else:
        # loop through the length of the string
        for i in range(len(string)):
            # within the loop we'll create three variables that will contain 
            # 1) each letter in our string, 2) take off the front of the string, and 
            # 3) a variable called back that will slice off the back of the string
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)

print(permute("ABCd", ""))

# Iterative approach
from math import factorial
def permutations(str):
    for p in range(factorial(len(str))):
        print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1] > str[i]:
            i -=1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i - 1] > str[q]:
                q += 1
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp
s = 'abc'
s = list(s)
permutations(s)
