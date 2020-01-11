"""
For this approach, we traverse the array.
We make absolute value of every element as an index as we are traversing the array.
We also make the value at this index as negative to mark it visited.
If something is already marked negative then this is the repeating element.
To find missing, traverse the array again and look for a positive value.
"""

def missing_repeating_element(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i]) - 1]> 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
        else:
            print('The number {} is the repeating number '.format(abs(arr[i])))
    print(arr)

    for i in range(len(arr)):
        if arr[i]>0:
            print(i + 1)
def main():
    arr = [3, 1, 3]
    missing_repeating_element(arr)
main()
