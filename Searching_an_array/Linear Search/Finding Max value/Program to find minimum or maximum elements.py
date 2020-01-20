"""
Given an array, write functions to find minimum and maximum elements in it.
"""
def get_min_max(arr):
    minimum, maximum = 1000000, -1000000
    for i in arr:
        if i < minimum:
            minimum = i
        elif i > maximum:
            maximum = i
    print("The minimum element is {} and the max is {}".format(minimum, maximum))
def get_min_max_method2(arr):
    minimum, maximum = arr[0], arr[0]
    for i in arr:
        minimum = min(i, minimum)
        maximum = max(i, maximum)
    print("The minimum and max elements are {} and {} respectively".format(minimum, maximum))

def main():
    arr1 = [12, 1234, 45, 67, 1 ]
    arr2 = [-1, 3, 4,2,3,1]
    get_min_max(arr2)
    get_min_max_method2(arr2)
main()
