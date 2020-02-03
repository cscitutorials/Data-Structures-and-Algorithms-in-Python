"""
Find lost element from a duplicated array
Given two arrays which are duplicates of each other except one element,
that is one element from one of the array is missing,
we need to find that missing element.
"""
def lost_element_duplicate_array(arr1, arr2):
    res = 0
    for i in range(len(arr1)):
        res ^= arr1[i]
    for i in range(len(arr2)):
        res ^= arr2[i]
    return res

def main():
    arr1 = [9, 4, 5]
    arr2 = [4, 5, 7, 9]
    print(lost_element_duplicate_array(arr1, arr2))
main()
