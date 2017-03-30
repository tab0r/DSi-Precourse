'''
                           Indexing and Slicing


Fill in each function below. There are 4 functions to complete.
Each function should be a one-liner unless otherwise specified.
You fill practice using index and slicing.

Run "python -m doctest assignment_1c.py" at the command line to test your work.
'''

###############################################################################
#######                     Looking at Strings
###############################################################################

def shift_on_character(string, char):
    '''
    INPUT: string, string
    OUTPUT: string

    Find the first occurence of the character char and return the string witth
    everything before char moved to the end of the string. If char doesn't
    appear, return the same string.

    This function may use more than one line.

    Example:
    >>> shift_on_character("galvanize", "n")
    'nizegalva'
    '''
    idx = string.find(char)
    return string[idx:]+string[0:idx]

def is_palindrome(string):
    '''
    INPUT: string
    OUTPUT: boolean

    Return whether the given string is the same forwards and backwards.

    Example:
    >>> is_palindrome("rats live on no evil star")
    True

    >>> is_palindrome("the moon waxes poetic in sunlight")
    False
    '''
    for i in range(len(string)):
        if string[i] != string[len(string)-1-i]: return False
    return True

###############################################################################
#######                     Looking at Lists
###############################################################################

def alternate(L):
    '''
    INPUT: list
    OUTPUT: list

    Use list slicing to return a list containing all the odd indexed elements
    followed by all the even indexed elements.

    Example:
    >>> alternate(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    ['b', 'd', 'f', 'a', 'c', 'e', 'g']
    '''
    A = L[1:len(L):2]
    B = L[0:len(L):2]
    return A + B

#some clever recursive function from people on the internet
def interleave(lst1, lst2):
    if not lst1:
        return lst2
    elif not lst2:
        return lst1
    return lst1[0:1] + interleave(lst2, lst1[1:])

def shuffle(L):
    '''
    INPUT: list
    OUTPUT: list

    Return the result of a "perfect" shuffle. You may assume that L has even
    length. You should return the result of splitting L in half and alternating
    taking an element from each.

    Example:
    >>> shuffle([1, 2, 3, 4, 5, 6])
    [1, 4, 2, 5, 3, 6]
    '''
    A = L[:len(L)//2]
    B = L[len(L)//2:]
    return interleave(A, B)
