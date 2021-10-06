from unittest.mock import patch
from itertools import islice

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()

def test_kill_mutant_inside_range(gen):
    with patch("color.sample") as mocksample:
        mocksample.side_effect = [[0, 0, 0]]
        c = next(gen)
        assert c == "#000000"
        assert len(c) == 7
        r_hex = c[1:3]
        g_hex = c[3:5]
        b_hex = c[5:7]
        r, g, b = int(r_hex, 16), int(g_hex, 16), int(b_hex, 16)
        assert r >= 0 and r < 256
        assert g >= 0 and g < 256
        assert b >= 0 and b < 256
        assert (r + g + b) >= 0 and (r + g + b) < 766
