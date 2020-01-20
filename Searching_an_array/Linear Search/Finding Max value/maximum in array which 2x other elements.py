"""
Maximum in array which is at-least twice of other elements
Given an array of integers of length n. Our task is to return
the index of the max element if the it is at least twice as much as every
other number in the array. If the max element does not satisfy the
condition return -1
"""

#Explanation. Find the 2 largest element.
#Check if it is greater than all the other elements

def max_element_that_is_2x_other_elements(arr):
    maximum = -10000
    second_max = -100000
    maximum_index = 0
    if len(arr) == 1:
        return 0
    for i in range(len(arr)):
        if arr[i]> maximum:
            second_max = maximum
            maximum = arr[i]
            maximum_index = i
        if arr[i] > second_max and arr[i] != maximum:
            second_max = arr[i]
    if maximum >=2*second_max:
        return maximum_index
    else:
        return -1
def main():
    arr1 = [3, 6, 1, 0]
    print(max_element_that_is_2x_other_elements(arr1))
main()
