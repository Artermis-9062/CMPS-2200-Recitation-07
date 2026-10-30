"""
Name: Chuong Hoang Pham
"""


def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    ###TODO
    if n == 1 or n == 0: return n

    return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)

def fib_top_down(n, fibs):
    ###TODO
    pass
    if n == 1 or n == 0: return n

    if fibs[n] != -1: 
        return fibs[n]
    else: 
        fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n-2, fibs)

    return fibs[n]


def fib_bottom_up(n):
    ###TODO
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


# counts = [0] * 11
# fib_recursive(10, counts)
# print(counts)
# print(sum(counts))