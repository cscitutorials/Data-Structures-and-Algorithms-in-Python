def find_mean(arr):
    if len(arr) <1:
        print("There is no array")
        return

    total = arr[0]
    for i in range(1, len(arr)):
        total += arr[i]
    mean = total/len(arr)
    print(mean)
def find_mean_recursion(arr, n):
    if n < 0:
        return "Does not exist"
    if n == 0:
        return arr[n]
    else:
        return arr[n] + find_mean_recursion(arr, n-1)
def mean(arr):
    n = len(arr) - 1
    total = find_mean_recursion(arr, n)
    mean_value = int(total)/len(arr)
    print(mean_value)


def main():
    arr = [1]
    find_mean(arr)
    mean(arr)
main()
