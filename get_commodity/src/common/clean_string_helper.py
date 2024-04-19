def remove_character(input_string: str, char: str, replace_with: str='') -> str:
    """
    Replaces the character/s within a string variable

    Args
    input_string - The string which has a character to 
        be replaced
    char - The character/s to be replaced within a string
    replace_with - The character to be inserted where char 
        is removed, default: ''
    """

    output_string = input_string.replace(char, replace_with)

    return output_string


def strip_whitespaces(input_string: str) -> str:
    """
    Removes trailing whitespaces within the string

    Args
    input_string - The string to be stripped off white spaces
    """

    return input_string.strip()