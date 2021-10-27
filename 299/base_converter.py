from string import ascii_uppercase, digits

BASE_SYSTEM_STRINGS =  {i:s  for i, s in  enumerate(digits+ascii_uppercase)}

def convert(number: int, base: int = 2) -> str:
    if base > 36 or base < 2:
        raise ValueError

    round_numerator = number
    bases = []
    while True:
        quotient, reminder = divmod(round_numerator, base) 
        bases.append(BASE_SYSTEM_STRINGS[reminder])
        round_numerator = quotient
        if round_numerator == 0:
            break
    
    return   "".join([digit for digit in bases ][::-1])