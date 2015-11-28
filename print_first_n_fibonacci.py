"""Print the first n finonacci numbers."""
from fibonacci.fibonacci import fib
import errno
import argparse

# Parse command line
parser = argparse.ArgumentParser(
    description="Print the first n fibonacci numbers, starting from zero")
parser.add_argument('limit', type=int)
args = parser.parse_args()

# Print the requested fibonacci numbers
try:
    for element in fib(args.limit):
        print(element)

# Ignore pipe signal errors (when piping to head, for example)
except IOError as e:
    if e.errno != errno.EPIPE:
        raise

