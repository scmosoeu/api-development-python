from typing import Literal

def get_current_value(str_value: str, split_by: str, remove_char: str=None) -> str:
    """
    Get current numeric value from the parsed in string value

    Args:
    str_value - The string value upon which the current
        value is going to be extracted 
    split_by - The characted withing string values that is
        going to be used to split the string
    remove_char default: None - Character within the string that
        is going to be removed  
    """

    value = str_value.split(split_by)[0]

    if remove_char is not None:
        
        value = value.replace(remove_char, '')

    return value


def get_mtd_value(str_value: str, split_by: str, remove_char: str=None) -> str:
    """
    Get month to date numeric value from the parsed in string value

    Args:
    str_value - The string value upon which the current
        value is going to be extracted 
    split_by - The characted withing string values that is
        going to be used to split the string
    remove_char default: None - Character within the string that
        is going to be removed  
    """

    value = str_value.split(split_by)[1]

    if remove_char is not None:
        
        value = value.replace(remove_char, '')

    return value


def convert_to_numeric(str_value: str, data_type: Literal['int', 'float']) -> int:
    """
    Convert the parsed string to a numeric value

    Args:
    str_value - The string value upon which the current
        value is going to be extracted 
    data_type - The data type the string is going to be
        converted to. Options: ('int', 'float')
    """

    if data_type == 'int':
        numeric_value = int(str_value)
    elif data_type == 'float':
        numeric_value = float(str_value)

    return numeric_value