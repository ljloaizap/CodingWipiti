'''PH'''

from challenges.challenge0 import main


def test_main_is_valid_number(capsys):
    '''PH'''
    main()
    stdout, _ = capsys.readouterr()

    arr_numbers = stdout.strip().split("\n")
    fixed_elements = arr_numbers[:2]
    assert fixed_elements == ['1', '2']


def test_main_prints_fizz_for_multiple_of_3(capsys):
    '''PH'''
    main()
    stdout, _ = capsys.readouterr()
    arr_numbers = stdout.strip().split("\n")
    for i, value in enumerate(arr_numbers):
        if (i+1) % 3 == 0 and (i+1) % 5 != 0:
            assert value == 'fizz'


def test_main_prints_fizz_for_multiple_of_5(capsys):
    '''PH'''
    main()
    stdout, _ = capsys.readouterr()
    arr_numbers = stdout.strip().split("\n")
    for i, value in enumerate(arr_numbers):
        if (i+1) % 5 == 0 and (i+1) % 3 != 0:
            assert value == 'buzz'


def test_main_prints_fizz_for_multiple_of_3_and_5(capsys):
    '''PH'''
    main()
    stdout, _ = capsys.readouterr()
    arr_numbers = stdout.strip().split("\n")
    for i, value in enumerate(arr_numbers):
        if (i+1) % 3 == 0 and (i+1) % 5 == 0:
            assert value == 'fizzbuzz'
