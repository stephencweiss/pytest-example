import pytest
from main import increment, divide, NonIntegerException


@pytest.mark.xfail(reason="not an integer!")
def test_increment():
    assert increment('0') == 1


@pytest.mark.xfail(raises=NonIntegerException)
def test_increment_xfail():
    assert increment('0') == 1


def test_increment_raises():
    with pytest.raises(NonIntegerException):
        increment('0') == 1

def test_increment_raises_general():
    with pytest.raises(Exception):
        increment('0') == 1
# def test_increment_raises_type():
#     with pytest.raises(TypeError):
#         increment('0') == 1


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_divide_xfail():
    assert divide(2, 0)
@pytest.mark.xfail(raises=Exception)
def test_divide_xfail_general():
    assert divide(2, 0)
@pytest.mark.xfail(raises=TypeError)
def test_divide_xfail_type():
    assert divide(2, 0)


def test_divide_raises():
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)
