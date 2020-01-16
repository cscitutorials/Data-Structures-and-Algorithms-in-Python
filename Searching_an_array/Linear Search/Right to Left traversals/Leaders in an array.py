"""
Write a program to print all the LEADERS in the array.
An element is leader if it is greater than all the elements to its right
side. And the rightmost element is always a leader.
For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.
Let the input array be arr[] and size of the array be size.
"""
def leaders_in_array(arr):
    n= len(arr)-1
    max_value = arr[n]
    print(max_value)
    for i in range(n, -1, -1):
        if arr[i] > max_value:
            max_value = arr[i]
            print(max_value)

def main():
    arr = [19, 17, 4, 3, 5, 2]
    leaders_in_array(arr)
main()
