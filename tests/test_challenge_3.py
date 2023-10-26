import pytest
import re
import string
from challenges.challenge3 import main


@pytest.mark.parametrize('length', [
    (-1), (7), (17)
])
def test_main_invalid_length(length):
    '''PH'''
    assert main(length=length) == "[Err] La longitud debe estar entre 8 y 16"


@pytest.mark.parametrize('with_mayus', [
    (True), (False)
])
def test_main_has_mayus(with_mayus):
    '''PH'''
    output = main(with_mayus=with_mayus)
    assert bool(re.search(r'[A-Z]', output)) == with_mayus


#@pytest.mark.parametrize('with_numbers', [
#    (True), (False)
#])
#def test_main_has_numbers(with_numbers):
#    '''PH'''
#    output = main(with_numbers=with_numbers)
#    assert bool(re.search(r'[0-9]', output)) == with_numbers


@pytest.mark.parametrize('with_symbols', [
    (True), (False)
])
def test_main_has_symbols(with_symbols):
    '''PH'''
    output = main(with_symbols=with_symbols)
    assert bool(
        re.search(f'[{re.escape(string.punctuation)}]', output)) == with_symbols


@pytest.mark.parametrize('has_mayus, has_numbers, has_symbols', [
    (True, True, True),
    (False, False, False)
])
def test_main_have_all_combined(has_mayus, has_numbers, has_symbols):
    '''PH'''

    pwd = main(16, has_mayus, has_numbers, has_symbols)
    assert bool(re.search('', pwd))
