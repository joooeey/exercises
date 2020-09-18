# -*- coding: utf-8 -*-

import pytest

class FibonacciSequence(list):

    def __init__(self):
        """Set the two initial elements of the sequence to 0 and 1."""
        super().__init__()
        self += [0, 1]

    def advance(self):
        """Add one more element to the end of the sequence."""
        self.append(self[-2] + self[-1])

    def __getitem__(self, i):
        """Return ith element of the sequence as in sequence[i]."""
        try:
            return super().__getitem__(i)
        except IndexError:
            self.advance()
            return self.__getitem__(i)

my_sequence = FibonacciSequence()

def get_fibonacci_number(n):
    """Return the nth Fibonacci number."""
    return my_sequence[n]

@pytest.mark.parametrize("index, output",
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                         [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
def test_fibonacci(index, output):
    """Test that the first few numbers are correct"""
    assert get_fibonacci_number(index) == output