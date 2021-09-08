'''A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given a number, n, determine and print whether it is Prime or Not prime.

Note: If possible, try to come up with a O(n***2) primality algorithm, or see what sort of optimizations you come up with for an O(n) algorithm. Be sure to check out the Editorial after submitting your code.
Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime'''

from math import sqrt

T = int(input())


def isPrime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i is 0:
            return False
    return True


for _ in range(T):
    n = int(input())
    
    if n >= 2 and isPrime(n):
        print("Prime")
    else:
        print("Not prime")