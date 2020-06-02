import pytest
from main import increment

@pytest.mark.xfail(reason="not an integer!")
def test_increment():
    assert increment('0') == 1