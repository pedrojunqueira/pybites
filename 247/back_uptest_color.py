from unittest.mock import patch
from itertools import islice

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


@pytest.mark.parametrize(
    "return_value, hexcode",
    [
        ([255, 255, 255], "#FFFFFF"),
        ([0, 0, 0], "#000000"),
    ],
)
def test_gen_hex_color(gen, return_value, hexcode):
    with patch("color.sample") as mocksample:
        mocksample.return_value = return_value
        c = next(gen)
        assert c == hexcode
        r_hex = hexcode[1:3]
        g_hex = hexcode[3:5]
        b_hex = hexcode[5:7]
        r, g, b = int(r_hex, 16), int(g_hex, 16), int(b_hex, 16)
        assert r >= 0 and r < 256
        assert g >= 0 and g < 256
        assert b >= 0 and b < 256
        assert (r + g + b) >= 0 and (r + g + b) < 766


def test_kill_mutant_inside_range(gen):
    with patch("color.sample") as mocksample:
        mocksample.side_effect = [[0, 0, 0]]
        c = next(gen)
        assert c == "#000000"
        r_hex = c[1:3]
        g_hex = c[3:5]
        b_hex = c[5:7]
        r, g, b = int(r_hex, 16), int(g_hex, 16), int(b_hex, 16)
        assert r >= 0 and r < 256
        assert g >= 0 and g < 256
        assert b >= 0 and b < 256
        assert (r + g + b) >= 0 and (r + g + b) < 766
    

def test_len_hex_color(gen):
    for hexcolor in islice(gen, 1000):
        assert len(hexcolor) == 7
        r_hex = hexcolor[1:3]
        g_hex = hexcolor[3:5]
        b_hex = hexcolor[5:7]
        r, g, b = int(r_hex, 16), int(g_hex, 16), int(b_hex, 16)
        assert r >= 0 and r < 256
        assert g >= 0 and g < 256
        assert b >= 0 and b < 256
        assert (r + g + b) >= 0 and (r + g + b) < 766


# def gen_hex_color():
#     while True:
#         r, g, b = sample(range(0, 256), 3)
#         yield '#{:02x}{:02x}{:02x}'.format(r, g, b).upper()