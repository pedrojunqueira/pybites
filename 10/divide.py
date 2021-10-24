def positive_divide(numerator, denominator):
    result = None
    try:
        result = numerator/denominator
    except ZeroDivisionError:
        return 0
    except TypeError as e:
        print(e)
    if result < 0:
        raise ValueError
    return result
