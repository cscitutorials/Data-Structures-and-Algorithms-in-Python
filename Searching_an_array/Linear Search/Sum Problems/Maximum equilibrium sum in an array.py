"""
The maximum equilibrium sum is the index where the value prefix sum is equal to
the suffix sum
Given an array arr[].
Find maximum value of prefix sum which is also suffix sum for index i in arr[].
Use this simple
arr3 = [0,2,5,1,1,0,0]
"""
#####   UNFINISHED #########
def max_equilibrium_sum(arr):
    total_sum = 0
    prefix_sum = 0
    max_value = -100000
    for i in range(len(arr)):
        total_sum += arr[i]
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == total_sum:
            max_value = max(prefix_sum, total_sum)
        total_sum -= arr[i]
    return max_value

def main():
    arr1 = [-1, 2, 3, 0, 3, 2, -1]
    arr2 = [-2, 5, 3, 1, 2, 6, -4, 2]
    arr3 = [0,2,5,1,1,0,0]
    print(max_equilibrium_sum(arr3))
main()
