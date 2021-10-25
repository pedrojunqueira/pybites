STAR = "*"


def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
    by row. So if width = 5 it should generate the following
    rows one by one:

    gen = gen_rhombus(5)
    for row in gen:
        print(row)

     output:
       *
      ***
     *****
      ***
       *
    """
    center = width
    for i in range(1, 2 * width, 2):
        if i > center:
            yield f"{(center-2)*STAR:^{width}}"
            center -= 2
        else:
            yield f"{i*STAR:^{width}}"
