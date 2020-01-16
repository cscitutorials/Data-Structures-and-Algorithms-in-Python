"""
Find the smallest and second smallest elements in
an array
"""
def find_the_two_smallest(arr):
    first, second = arr[0], arr[0]
    for i in range(len(arr)):
        if arr[i] < first:
            second = first
            first = arr[i]
        if arr[i] < second and first != arr[i]:
            second = arr[i]
    print("The smallest elment is {} and the second is {}".format(first, second))

def main():
    arr = [12, 13, 1, 10, 34, 1]
    find_the_two_smallest(arr)
main()
