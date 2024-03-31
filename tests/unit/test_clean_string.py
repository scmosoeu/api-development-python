from common.clean_string_helper import remove_character, strip_whitespaces


def test_remove_character():

    input_string = 'R10.00'
    expected_output = '10.00'

    output = remove_character(input_string, 'R', '')

    assert output == expected_output


def test_remove_punc():

    input_string = '100,000.00'
    expected_output = '100000.00'

    output = remove_character(input_string, ',', '')

    assert output == expected_output


def test_stripwhitespaces():

    input_string = '  200.00 '
    expected_output = '200.00'

    output = strip_whitespaces(input_string)

    assert output == expected_output