HTML_SPACE = '&nbsp;'


def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    value_length = len(str(value))
    fill_spaces = (column_length - value_length) 
    return f'{fill_char*fill_spaces}{value}'