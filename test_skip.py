import pytest
from main import increment

CONDITION = True

@pytest.mark.skip(reason="no way to currently test")
def test_increment():
    assert increment(0) == 1

@pytest.mark.skipif(CONDITION == False, reason="Condition is False")
def test_increment_skip1():
    assert increment(0) == 1

@pytest.mark.skipif(CONDITION == True, reason="Condition is True")
def test_increment_skip2():
    assert increment(0) == 1