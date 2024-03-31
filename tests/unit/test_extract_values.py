from common.extract_values import get_current_value


def test_get_current_values_first():
    
    input_string = 'R10.00MTD:R70.00'
    expected_output = 'R10.00'
    output = get_current_value(input_string, 'MTD:', 0)

    assert output == expected_output


def test_get_current_values_second():
    
    input_string = 'R10.00MTD:R70.00'
    expected_output = 'R70.00'
    output = get_current_value(input_string, 'MTD:', 1)

    assert output == expected_output