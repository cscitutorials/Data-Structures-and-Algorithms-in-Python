"""
Binary search is used to find an item in a sorted array. If the array is sorted
the most efficient way will be to use a sorted array.
There are two methods to do a binary search:
Method 1: iterative method using while loop
Method 2: Recursive method
"""
def recursive_binary_search(array, element, left, right):
    if right<left:
        return -1
    mid = int((left + right)/2)
    if array[mid] == element:
        print("hello ", mid)
        return mid
    if array[mid] < element:
        return recursive_binary_search(array, element, mid + 1, right)
    return recursive_binary_search(array, element, left, mid - 1)

def iterative_binary_search(array, item):
    l = 0
    r = len(array) - 1
    while l<=r:
        mid = int((l+r)/2)
        if array[mid] == item:
            return mid
        elif array[mid] < item:
            l = mid + 1
        else:
            r = mid - 1
    return -1



def main():
    arr = [3, 4, 5, 6, 8, 9, 10]
    x = 6
    n = len(arr) - 1
    print("The recursive method ", recursive_binary_search(arr, x, 0, n))
    print("The iterative method ", iterative_binary_search(arr, x))
main()
