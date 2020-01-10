"""
The two pointer technique is used to find pairs in a sorted array
"""
# Given an array sorted in ascending order, find if there exists any pair that
# sums to a given value.

def two_pointer(array, value):
    left = 0
    right = len(array)-1
    while left<right :
        if array[left] + array[right] == value:
            print ("The two elements are {} and {} ".format(array[left], array[right]))
            return True
        elif array[left] + array[right] < value:
            left += 1
        else:
            right -= 1
    return False

def main():
    arr = [3, 5, 8, 9, 10, 11, 15]
    value = 20
    two_pointer(arr, value)
main()
