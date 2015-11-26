from itertools import islice

def fibonacci(n=None):
    """Return a generator of elements from the fibonacci sequence.

    Args:
        n: (optional) if provided, limit the number of generated elements to n,
        otherwise the generator will produce the infinite sequence
        Returns:
            a generator over the fibbonacci numbers (starting from 0)
    """
    def fibonacci_generator():
        a=0
        b=1
        while True:
            yield a
            a,b=b,a+b

    return islice(fibonacci_generator(), n)

