from typing import List  # not needed when we upgrade to 3.9

TEMPLATE = "| {name}"


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    for i in range(0, len(names), cols):
        line = [f"{TEMPLATE.format(name=name):<12}" for name in names[i : i + cols]]
        print("".join(line))
