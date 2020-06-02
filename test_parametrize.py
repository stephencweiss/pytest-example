import pytest
from main import increment

@pytest.mark.parametrize(
    ("n","expected"),
    [
         (1, 2),
         (4, 5),
         (-1, 0),
    ],
)
def test_increment(n, expected):
    assert increment(n) == expected
