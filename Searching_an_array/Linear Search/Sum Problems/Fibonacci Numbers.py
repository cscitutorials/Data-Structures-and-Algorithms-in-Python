def fibonacci_numbers(n):
    if n <0:
        return "Incorrect input of n"
    if n <= 1: #if n ==0: return 0 or if n==1: return n
        return n
    else:
        return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)

def main():
    n = 10
    print(fibonacci_numbers(n))
main()
