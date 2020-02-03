"""
Find the Number Occurring Odd Number of Times
Given an array of positive integers. All numbers occur even number of times
except one number which occurs odd number of times. Find the number in O(n)
time & constant space.
"""
def odd_number(arr):
    res = 0
    n = len(arr)
    for i in range(0, n):
        res ^= arr[i]
    return(res)

def main():
    arr = [1, 2, 3, 2, 3, 1, 3]
    print(odd_number(arr))
main()
