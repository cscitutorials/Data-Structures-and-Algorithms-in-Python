"""
Maximum triplet sum in array
Given an array, the task is to find maximum triplet sum in
 the array.
 """

def maximum_triplet(arr):
    first, second, third = -1000, -1000, -1000
    for i in range(len(arr)):
        if arr[i]> first:
            third = second
            second = first
            first = arr[i]
        elif arr[i]>second and first != arr[i]:
            third = second
            second = arr[i]
        elif arr[i]>third and second != arr[i]:
            third = arr[i]
    max_sum = first + second + third
    print("first is {}, second is {}, third is {}, sum is {}".format(first, second, third, max_sum))
def main():
    arr1 = [1, 2, 3, 0, -1, 8, 10]
    arr2 = [9, 8, 20, 3, 4, -1, 0]
    arr3 = [3,3,3,3, 1]
    maximum_triplet(arr2)
main()
