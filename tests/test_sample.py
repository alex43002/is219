"""
Module-level docstring describing the purpose of the test module.
"""

from app import inc, sub

def test_increase():
    """
    Test the inc function.
    """
    assert inc(4) == 5
    assert inc(6) == 7

def test_decrease():
    """
    Test the sub function.
    """
    assert sub(5) == 4
    assert sub(2) == 1
