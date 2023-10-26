'''PH'''
import pytest
from challenges import challenge4


def test_main():
    '''PH'''
    assert challenge4.main() == 'asd'


@pytest.mark.parametrize('number, expected', [
    (0, None),
    (2, True),
    (3, True),
    (8, False),
    (24, False)
])
def test_is_prime_number(number, expected):
    '''PH'''

    assert challenge4.is_prime_number(number) == expected


@pytest.mark.parametrize('number, expected', [
    (-1, None),
    (0, True),
    (4, False),
    (8, True),
    (13, True),
    (20, False),
    (21, True),
    (22, False)
])
def test_is_fibonacci_number(number, expected):
    '''PH'''
    assert challenge4.is_fibonacci_number(number) == expected


@pytest.mark.parametrize('number, expected', [
    (-1, False),
    (0, True),
    (7, False),
    (30, True),
    (-4, True)
])
def test_is_even_number(number, expected):
    '''PH'''
    assert challenge4.is_even_number(number) == expected
