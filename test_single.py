import pytest
from main import increment

def test_increment():
    assert increment(0) == 1