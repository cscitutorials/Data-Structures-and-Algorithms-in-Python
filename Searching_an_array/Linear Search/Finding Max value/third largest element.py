"""
Third largest element in an array of distinct elements
Given an array of distinct elements, find third largest
element in it.
"""
def third_largest_element(arr):
    first, second,third = -100000000,-100000000,-100000000
    for i in range(len(arr)):
        if arr[i]> first:
            third = second
            second = first
            first = arr[i]
        elif arr[i]>second and first != arr[i]:
            third = second
            second = arr[i]
        elif arr[i] > third and second != arr[i]:
            third = arr[i]
    print("The third largest element is {}.".format(third))
def main():
    arr1 = [1, 14, 2, 16, 10, 20]
    arr2 = [19, -10, 20, 14, 2, 16, 10]
    third_largest_element(arr2)
main()
