from common.numeric_conversion import convert_to_numeric


def test_convert_to_numeric_int():

    input_string = '123.00'
    
    output = convert_to_numeric(input_string, 'int')

    assert isinstance(output, int)


def test_convert_to_numeric_float():

    input_string = '123.00'
    
    output = convert_to_numeric(input_string, 'float')

    assert isinstance(output, float)