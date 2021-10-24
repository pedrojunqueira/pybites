def positive_divide(numerator, denominator):
    """
    when denominator is 0 catch the corresponding exception and return 0.
    when numerator or denominator are not of the right type reraise the corresponding exception.
    if the result of the division (after surviving the exceptions) is negative, raise a ValueError
    """
    if denominator==0:
        print("zero")
    if any( n is not isinstance(n,int) or n is not isinstance(n, float) for n in [numerator, denominator]):
        print("Error")


positive_divide(1,0)