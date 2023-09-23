'''PH'''
import pytest
from challenges.challenge1 import main


@pytest.mark.parametrize('text, transformed', [
    ('hello', '#3110'),
    ('siete', '51373'),
    ('voĉe', r'\/0Ĉ3'),
    ('leet', '1337'),
    ('', ''),
    (None, None)
])
def test_main(text, transformed):
    '''PH'''
    assert main(text) == transformed
