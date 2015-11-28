from itertools import islice

def fib(limit=None):
    """Return a generator of elements from the fibonacci sequence.

    Args:
        limit: (optional) if provided, limit the number of generated elements to 'limit',
        otherwise the generator will produce the infinite sequence
    Returns:
        a generator over the fibbonacci numbers (starting from 0)
    Throws:
        ValueError, if 'limit' is not None or an integer: 0 <= x <= sys.maxsize
    """
    def fibonacci_generator():
        a = 0
        b = 1
        while True:
            yield a
            a, b = b, a+b

    return islice(fibonacci_generator(), limit)

