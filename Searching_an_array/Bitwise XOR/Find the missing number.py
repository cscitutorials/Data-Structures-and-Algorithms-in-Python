"""
Find the Missing Number
You are given a list of n-1 integers and these integers are in the
range of 1 to n. There are no duplicates in the list. One of the integers
is missing in the list. Write an efficient code to find the missing integer.
"""

def missing_number(arr):
    """
    solution is to xor all arr elements
    xor numbers for n+1 integers
    xor both results
    """
    res = 0
    result = 0
    for i in range(len(arr)):
        res ^= arr[i]
    for i in range(len(arr) + 1):
        result ^= i
    print(res ^ result)

def main():
    arr = [3,0,1]
    arr = [1,2,4,3]
    missing_number(arr)
main()
