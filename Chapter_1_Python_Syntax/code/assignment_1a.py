'''
                     List comprehension and map function

Fill in each function below (there are 7).
Each function should be a one-liner.
You fill practice using 'map' and list comprehension with various datatypes.

Run "python -m doctest assignment_1a.py" at the command line to test your work.
'''
import numpy as np
import pdb
import string
###############################################################################
#######                     Looking at Lists and Matrices
###############################################################################
def average_rows1(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats

    Use list comprehension to take the average of each row in the matrix and
    return it as a list.

    Example:
    >>> average_rows1([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    '''
    avgs = [sum(row)/len(row) for row in mat]
    return avgs

def average_rows2(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats

    Use map to take the average of each row in the matrix and
    return it as a list.

    Example:
    >>> average_rows1([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    '''
    a = list(map(np.mean, mat))
    return a

def sort_rows(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: 2 dimensional list of integers (matrix)

    Use list comprehension to modify each row of the matrix to be sorted.
    Notice that the matrix is modified in place

    Example:
    >>> M = [[4, 5, 2, 8], [3, 9, 6, 7]]
    >>> sort_rows(M)
    >>> M
    [[2, 4, 5, 8], [3, 6, 7, 9]]
    '''
    for row in mat:
        row.sort()

###############################################################################
#######                     Looking at Strings
###############################################################################
def word_lengths1(phrase):
    '''
    INPUT: string
    OUTPUT: list of integers

    Use list comprehension to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.

    Example:
    >>> word_lengths1("Welcome to the Data Science Immersive Program!")
    [7, 2, 3, 4, 7, 9, 8]
    '''
    return [len(word) for word in phrase.strip().split(' ')]

def word_lengths2(phrase):
    '''
    INPUT: string
    OUTPUT: list of integers

    Use map to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.

    Example:
    >>> word_lengths2("Welcome to the Data Science Immersive Program!!")
    [7, 2, 3, 4, 7, 9, 9]
    '''
    return list(map(len, phrase.strip().split(' ')))

###############################################################################
#######                     Looking at Integers
###############################################################################
def even_odd0(x):
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'


def even_odd1(L):
    '''
    INPUT: list of integers
    OUTPUT: list of strings

    Use list comprehension to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.

    Example:
    >>> even_odd1([6, 4, 1, 3, 8, 5])
    ['even', 'even', 'odd', 'odd', 'even', 'odd']
    '''
    # returns even correctly, not sure how to make it return odd
    return [even_odd0(x) for x in L]

def even_odd2(L):
    '''
    INPUT: list of integers
    OUTPUT: list of strings

    Use map to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.

    Example:
    >>> even_odd2([6, 4, 1, 3, 8, 5])
    ['even', 'even', 'odd', 'odd', 'even', 'odd']
    '''
    return list(map(even_odd0, L))
