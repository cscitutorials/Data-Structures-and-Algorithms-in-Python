def total_product(arr):
    if len(arr) == 0:
        print("M1 incorrect")
        return
    total = 1
    for i in range(len(arr)):
        total *= arr[i]
    print(total)

def total_product_recursion(arr, n):
    if n<0:
        return"Incorrect Rec"
    if n==0:
        return arr[n]
    else:
        return arr[n] * total_product_recursion(arr, n-1)
def main():
    arr = [2,2,1,2]
    n = len(arr) - 1
    total_product(arr)
    print(total_product_recursion(arr, n))
main()
