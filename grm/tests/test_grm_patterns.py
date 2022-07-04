"""
    GRM package
    Tests for grm.patterns
"""

# global imports
import pytest

# local imports
from ..patterns import Singleton


def test_grm_patterns_singleton():
    """ Test singleton pattern """

    class TestSingleton(metaclass=Singleton):
        pass

    test_singleton_1 = TestSingleton()
    test_singleton_2 = TestSingleton()

    assert id(test_singleton_1) == id(test_singleton_2), "Singleton instances must be the same"
