"""
When searching in an unsorted array, we use a linear traversal by searching from
the first element to the last element.
There are three methods/techniques we can use to search in an unsorted array.
Method 1: Using a for loop (first to last vice versa)
Method 2: Using a while loop (first to last vice versa)
Method 3: Recursion (first to last vice versa)
We can either print, return, store or make a boolean value to be true
"""

#Method 1
"""
Given an unsorted array of integers, find the index of an element in the array.
"""
def linear_search_m1(my_array, k):
    for i in range(len(my_array)):
        if my_array[i] == k:
            print('Method 1 finds ' + str(k) + ' at index ' + str(i))
            #Find the other method for string formatting.
            break
    return -1

def l_search_while_loop(this_array, x):
    l = 0
    r = len(this_array)
    while l<r:
        if this_array[l] == x:
            return l
        l += 1
    return -1

def recursive_linear_search(arr, element, l):
    n = len(arr)
    if l == n:
        return -1
    if arr[l] == element:
        print("Found recusively at ", l)
        return l
    return recursive_linear_search(arr, element, l+1)

def main():
    my_array = [3,1,5,6,3,9,2,4]
    k = 4
    linear_search_m1(my_array, k)
    print(l_search_while_loop(my_array, k))
    recursive_linear_search(my_array, k, 0)
main()
