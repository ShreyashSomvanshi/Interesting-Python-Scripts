def isPrime(Number):  # slow
    return 2 in [Number, 2 ** Number % Number]


def isprime(n):  # out of memory errors with big numbers
    """check if integer n is a prime"""
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
        # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def is_prime(n):  # Best until now
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        # print '\t', f
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True
