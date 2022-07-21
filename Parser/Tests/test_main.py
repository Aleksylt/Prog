import pytest

from main import a_plus_b, a_minus_b


def test_a_plus_b():
    assert a_plus_b(2, 3) == 5, "что-то не так,  2 + 3 != 5 !!!"
    assert a_plus_b(2, 2) != 5
    with pytest.raises(TypeError):
        a_plus_b("1","2")


def test_a_minus_b():
    assert a_minus_b(3, 2) == 1, "что-то не так"
    assert a_minus_b(3, 2) != 0
    with pytest.raises(TypeError):
        a_minus_b("1","2")

