

def find_equilibrium_index(arr):
    total_sum = 0
    prefix_sum = 0
    max_value = -100000
    max_index = -1
    for i in range(len(arr)):
        total_sum += arr[i]
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == total_sum:
            max_value = prefix_sum
            max_index = i
            print('The index is ', max_index)
            print('max value is ', max_value)
        total_sum -= arr[i]
    if max_value == -100000:
        print("there was no equilibrium in this array")

def main():
    arr1 = [-1, 2, 3, 0, 3, 2, -1]
    arr2 = [-2, 5, 3, 1, 2, 6, -4, 2]
    arr3 = [0,2,5,1,1,0,0]
    arr4 = [-7, 1, 5, 2, -4, 5, 0,2]
    arr5 = [-7, 1, 5, 2, -4, 3, 0]
    # print(equilibrium_index(arr1))
    find_equilibrium_index(arr5)
main()
