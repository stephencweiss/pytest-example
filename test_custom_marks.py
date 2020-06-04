import pytest
from main import increment

@pytest.mark.mark_one()
def test_increment_one():
    assert increment(0) == 1


@pytest.mark.mark_two()
def test_increment_two():
    assert increment(0) == 1


# @pytest.mark.mark_three()
# def test_increment_three():
#     assert increment(0) == 1