from functools import lru_cache

@lru_cache
def cached_fib(n):
    if n < 0:
        raise ValueError
    elif n in (0, 1):
        return n
    else:
        return(cached_fib(n-1) + cached_fib(n-2))