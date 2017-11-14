import pytest

from conftest import Sample, RefactoredSample

def test_sample_here():
    test = Sample("Test")
    print(test)

def test_another_sample_here():
    test = RefactoredSample("Test")
    print(test)
