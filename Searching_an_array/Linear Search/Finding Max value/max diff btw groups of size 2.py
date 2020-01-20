"""
Maximum difference between groups of size two
Given an array of even number of elements,
form groups of 2 using these array elements such that the difference
between the group with highest sum and the one with lowest sum is maximum.

Note: An element can be a part of one group only and it has to be a part of at
least 1 group.
"""
def max_diff_btw_groups_of_size_two(arr):
    highest_num = -1000000
    second_high = -1000000
    lowest_num = 1000000
    second_low = 1000000
    for i in range(len(arr)):
        if arr[i] > highest_num:
            second_high = highest_num
            highest_num = arr[i]
        if arr[i] > second_high and arr[i] != highest_num:
            second_high = arr[i]
        if arr[i] < lowest_num:
            second_low = lowest_num
            lowest_num = arr[i]
        if arr[i] < second_low and arr[i] != lowest_num:
            second_low = arr[i]
    return abs(highest_num + second_high) - abs(lowest_num + second_low)

def main():
    arr = [1, 4, 9, 6]
    arr2 = [6, 7, 1, 11]
    print(max_diff_btw_groups_of_size_two(arr2))
main()
