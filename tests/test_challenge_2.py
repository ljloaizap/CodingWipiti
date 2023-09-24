'''PH'''
import pytest
from challenges.challenge2 import main


@pytest.mark.parametrize('sequence, expected', [
    (None, 'E-ST'),
    (123, 'E-ST'),
    (False, 'E-ST'),
    ('', 'E-NENV'),
    (' ', 'E-NM'),
    ('a', 'E-NM'),
    ('P1,', 'E-NM'),
    ('P1,P2,P1,,,,', 'E-NM'),
    ('P1', 'I-OK')
])
def test_main_return_code(sequence, expected):
    '''PH'''
    assert main(sequence) == expected


@pytest.mark.parametrize('sequence, expected', [
    ('P1, P2, P1, P2', 'Deuce'),
    ('P1, P1, P1, P2, P2, P2', 'Deuce')
])
def test_main_deuce(capsys, sequence, expected):
    '''PH'''
    # main('P1, P2')
    main(sequence)
    stdout, _ = capsys.readouterr()
    last_line = stdout.split('\n')[-2]
    # assert last_line == "> Deuce"
    assert last_line == f"> {expected}"


def test_main_rabbit(capsys):
    '''PH'''
    main('P1')
    stdout, _ = capsys.readouterr()
    # last_line = stdout.split('\n')[-1]
    assert stdout == "> rabbit\n"
