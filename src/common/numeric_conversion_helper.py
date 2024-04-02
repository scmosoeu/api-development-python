from typing import Literal, Union


def convert_to_numeric(str_value: str, data_type: Literal['int', 'float']) -> Union[int, float]:
    """
    Convert the parsed string to a numeric value

    Args:
    str_value - The string value upon which the current
        value is going to be extracted 
    data_type - The data type the string is going to be
        converted to. Options: ('int', 'float')
    """

    if data_type == 'int':
        numeric_value = int(float(str_value))
    elif data_type == 'float':
        numeric_value = float(str_value)

    return numeric_value