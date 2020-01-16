def find_sum_recursive_method(arr,n):
    if n == 0:
        return arr[n]
    else:
        return arr[n] + find_sum_recursive_method(arr, n -1)

def find_sum_iterative_method(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    print(total)

def main():
    arr = [1,2,3]
    # print(find_sum_recursive_method(arr, 0, 0 ))
    find_sum_iterative_method(arr)
    print(find_sum_recursive_method(arr, 2))
main()
