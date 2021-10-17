# the printb python module

This is a small wrapper around the [python-bid](https://pypi.org/project/python-bidi/)

It has the following api:

```printb.printb(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)```

Adds a wrapper for python built-in [print](https://docs.python.org/3/library/functions.html#print) If any one of the arguments passed via ```*objects``` is a string, then swap it with 
[bidi.algorithm.get_display](https://pypi.org/project/python-bidi/)

```printb.input([prompt])```

Adds a wrapper for python built-in [input](https://docs.python.org/3/library/functions.html#input), when a prompt string argument is passed then it is swapped before printing
 
## Example usage

See the test-bidi.py file for example usage.