from unittest.mock import patch
from itertools import islice

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


# def test_gen_hex_color(gen):
#     with patch("color.sample") as mocksample:
#         mocksample.side_effect = [[255, 255, 255],[1, 1, 1]]
#         c = next(gen)
#         assert c == "#FFFFFF"
#         c = next(gen)
#         assert c == "#010101"


# def test_len_hex_color(gen):
#     sampling = []
#     for hexcolor in islice(gen, 100000):
#         assert len(hexcolor) == 7
#         r_hex = hexcolor[1:3]
#         g_hex = hexcolor[3:5]
#         b_hex = hexcolor[5:7]
#         r, g, b = int(r_hex, 16), int(g_hex, 16), int(b_hex, 16)
#         assert r >= 0 and r < 256
#         assert g >= 0 and g < 256
#         assert b >= 0 and b < 256
#         assert (r + g + b) >= 0 and (r + g + b) < 766
#         sampling.append(r)
#         sampling.append(g)
#         sampling.append(b)
#     sampling_set = set(sampling)
#     for i in range(0,256):
#         assert i in list(sampling_set)


@patch.object(color, "sample", side_effect=[[191, 165, 216], [101, 102, 103]])
def test_gen_hex_color(mock, gen):
    assert next(gen) == "#BFA5D8"
    assert next(gen) == "#656667"
