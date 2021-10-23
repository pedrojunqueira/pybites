ROMANS = "IVXLCDM"


def dec_to_roman(number, roman):
    if number == "0":
        return ""
    if number in ["1", "2", "3"]:
        return int(number) * roman[0]
    if number == "4":
        return roman[:2]
    if number == "5":
        return roman[1]
    if number in ["6", "7", "8"]:
        return roman[1] + (int(number) - 5) * roman[0]
    else:
        return roman[0] + roman[2]


def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    if not isinstance(decimal_number, int):
        raise ValueError
    if not decimal_number > 0 and decimal_number < 4000:
        raise ValueError
    decimal_str = [str(n) for n in str(decimal_number)]

    roman_system = [ROMANS[i : i + 3] for i in range(0, len(ROMANS), 2)]

    decimals_to_iterate = roman_system[: len(decimal_str)][::-1]

    result = ""
    for number, roman in zip(decimal_str, decimals_to_iterate):
        result += dec_to_roman(number=number, roman=roman)
    return result

print(romanize(1976))