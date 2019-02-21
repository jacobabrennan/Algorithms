#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None, allowed_hops=[1, 2, 3]):
    if(n == 0):
        return 1
    # Check cache
    if(not cache):
        cache = [0] * (n+1)
    try:
        if(cache[n]):
            return cache[n]
    except:
        print(F'Error on {n}')
    # Calculate total number of ways to climb n steps
    ways = 0
    for hop in allowed_hops:
        if(hop > n):
            continue
        steps_left = n - hop
        ways += climbing_stairs(steps_left, cache, allowed_hops)
    # Store result in cache and return
    cache[n] = ways
    return ways


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        msg = "There are {ways} ways for a child to jump {n} stairs."
        print(msg.format(ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
