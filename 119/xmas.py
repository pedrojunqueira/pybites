def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
    Each row has row_number*2-1 stars, simple example: for rows=3 the
    output would be like this (ignore docstring's indentation):
    *
    ***
    *****"""
    tree_rows = [f"{(i*2-1)*'*':^{rows*2}}\n" for i in range(1, rows + 1)]
    return "".join(tree_rows).strip("\n")
