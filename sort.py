#!/usr/bin/python
import random

class InvalidInputException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def merge_sort(array):
    """ Sorts the input array of integers in descending order using the
    merge sort algorithm with runtime nlogn.
    """
    if array == None:
        raise InvalidInputException("Empty list.")
    n = len(array)
    if n <= 1:
        return array
    mid = int(n/2) + 1
    left = merge_sort(array[:mid-1])
    right = merge_sort(array[mid-1:])
    return merge(left,right)

def merge(A,B):
    """ Helper method for merge_sort that coordinates the merging of two groups
    of numbers.
    """
    result = []
    aIndex = 0
    bIndex = 0
    while aIndex < len(A) and bIndex < len(B):
        if A[aIndex] >= B[bIndex]:
            result.append(A[aIndex])
            aIndex += 1
        else:
            result.append(B[bIndex])
            bIndex += 1
    if aIndex < len(A):
        result += A[aIndex:len(A)]
    if bIndex < len(B):
        result += B[bIndex:len(B)]
    return result


def quick_sort(array):
    """ Sorts the input array of integers in descending order using the
    quicksort algorithm with expected runtime nlogn.
    """
    if array == None:
        raise InvalidInputException("Empty list.")
    if len(array) <= 1:
        return array
    pivot = random.choice(array)
    L = []
    E = []
    G = []
    for num in array:
        if num < pivot:
            L.append(num)
        elif num > pivot:
            G.append(num)
        else:
            E.append(num)
    return quick_sort(G) + E + quick_sort(L)


def radix_sort(array):
    """ Sort the input array of integers in descending order using the
    radixsort algorithm with runtime nd (with d being max # of digits).
    """
    if array == None:
        raise InvalidInputException("Empty list.")
    if len(array) <= 1:
        return array
    buckets = [[],[],[],[],[],[],[],[],[],[],[]]
    min_num = 0
    if min(array) < 0:
        max_digit = len(str(max(array))) - 1
        min_num = min(array)
        for i in range(0,len(array)):
            array[i] = array[i] - min_num
    max_digit = len(str(max(array)))
    A = array
    for place in range(0,max_digit):
        for num in A:
            digit = int(num/10**(place))%10
            buckets[digit].append(num)
        A = []
        for i in range(9,-1,-1):
            A.extend(buckets[i])
        buckets = [[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(0,len(A)):
        A[i] = A[i] + min_num
    return A
