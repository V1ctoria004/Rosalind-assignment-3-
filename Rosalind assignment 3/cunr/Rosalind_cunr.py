def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * double_factorial(n - 2)


n = int(open('rosalind_cunr.txt').readline())
print (double_factorial(2 * n - 5) % 1000000)