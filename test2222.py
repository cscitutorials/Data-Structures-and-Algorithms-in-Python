def insert_binary_search(arr, x):
    l = 0
    r = len(arr)-1
    if arr[0]>x:
        return 0
    if arr[r-1]<x:
        return r
    while l<=r:
        mid = int((l +r)/2)
        if arr[mid] > x and x > arr[mid - 1]:
            return mid
        elif x > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1
def main():
    arr = [1, 2, 4, 5, 6]
    target = 3
    pos = insert_binary_search(arr, target)
    arr.insert(pos, 3)
    print(arr)
main()
