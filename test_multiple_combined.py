import pytest
from main import increment

CONDITION = True
multiple_marks = [pytest.mark.skipif(CONDITION == True,reason="Multiple marks, condition is True"), pytest.mark.xfail(reason="non integer")]

@pytest.mark.parametrize(
    ("n","expected"),
    [
         (1, 2),
         (4, 5),
         pytest.param(-1, 0, marks=pytest.mark.skip(reason="because we want to")),
         pytest.param(-1, 0, marks=pytest.mark.skipif(CONDITION == True,reason="Condition is True")),
         pytest.param(-1, 0, marks=pytest.mark.skipif(CONDITION == False, reason="Condition is False")),
         pytest.param('a', 'a', marks=multiple_marks),
         pytest.param('a', 'a', marks=pytest.mark.xfail(reason="non integer")),
         pytest.param(0, 0, marks=pytest.mark.xfail(reason="did not increment"))
    ],
)
def test_increment(n, expected):
    assert increment(n) == expected


@pytest.mark.skipif(CONDITION == True,reason="Condition is True")
@pytest.mark.xfail(reason="non-integer")
def test_increment_single_true():
    assert increment('0') == 1


@pytest.mark.skipif(CONDITION == False,reason="Condition is False")
@pytest.mark.xfail(reason="non-integer")
def test_increment_single_false():
    assert increment('0') == 1