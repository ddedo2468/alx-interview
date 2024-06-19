#!/usr/bin/python3
"""
prime time
"""


def isWinner(x, nums):
    """
    main fnction for prime game module
    """
    maria = 0
    ben = 0

    def SieveOfEratosthenes(n):
        """Sieve of Eratosthenes Function"""

        prime = [True for i in range(n + 1)]
        pointer = 2
        while pointer * pointer <= n:
            if prime[pointer] is True:
                for i in range(pointer * pointer, n + 1, pointer):
                    prime[i] = False
            pointer += 1
        prime[0] = False
        prime[1] = False
        return prime
