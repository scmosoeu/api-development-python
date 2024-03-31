from common.clean_string import remove_character, strip_whitespaces


def get_current_value(str_value: str, split_by: str, index_loc: int) -> str:
    """
    Get current numeric value from the parsed in string value

    Args:
    str_value - The string value upon which the current
        value is going to be extracted 
    split_by - The characted withing string values that is
        going to be used to split the string
    index_loc - Location of the extracted value within an 
        iterable
    """

    value = str_value.split(split_by)[index_loc]

    return value
