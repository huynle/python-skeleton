import pytest

from .conftest import sample


def test_sample_here():
    test = sample.core.CoreSample("Test")
    print(test)
