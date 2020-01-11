"""
The bitwise XOR operator is the most useful operator from technical interview
 perspective. It is used in many problems. It is used to find the repeating
 element or the element appearing once.
"""
#Given an array, find the repeating element
def single_occurring_element(array):
    output = 0
    for i in range(len(array)):
        output ^= array[i]
    print(output)

def repeating_element(arr):
    """
    Given an array where every element appears once, find the
    repeating_element
    """
    pass
    
def main():
    arr = [3,1,3]
    single_occurring_element(arr)
main()
