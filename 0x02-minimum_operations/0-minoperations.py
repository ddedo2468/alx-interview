#!/usr/bin/python3
""" Find the minimum operations """


def minOperations(n):
    """
        @n: number of characters
        Return: minimum operations to copy pasta to reach n
    """
    # current: what we have in the note bad
    current = 1
    # count: how many ops have we done
    count = 0
    # clipboard: it's what we have in the clippoard
    # like if we paste how many chars will be pasted
    clipboard = 0

    while current < n:
        rest = n - current

        if rest % current == 0:
            clipboard = current
            current += clipboard
            count += 2
        else:
            current += clipboard
            count += 1
    return count
