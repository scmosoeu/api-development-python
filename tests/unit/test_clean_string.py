from common.clean_string import remove_character, strip_whitespaces


def test_remove_character():

    input_string = 'R10.00'
    expected_output = '10.00'

    output = remove_character(input_string, 'R', '')

    assert output == expected_output