def fibonacci_numbers(n):
    if n <0:
        return "Incorrect input of n"
    if n <= 1:
        return n
    else:
        return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)

def main():
    n = 9
    print(fibonacci_numbers(n))
main()
