"""
We have a sorted array with duplicate elements and we have to find the index of
last duplicate element and print index of it and also print the duplicate
element. If no such element found print a message.
"""
def find_last_duplicate(arr):
    n = len(arr) - 1
    for i in range(n, 0, -1):
        if arr[i] == arr[i-1]:
            print(arr[i], i)
            return

def main():
    arr =[1,1, 5, 6, 3, 7]
    find_last_duplicate(arr)
main()
