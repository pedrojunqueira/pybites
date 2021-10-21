import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize(
    "typerr",
    [
        [True, False],
        ["1", 2],
        ["3"],
    ],
)
def test_raise_type_errors(typerr):
    with pytest.raises(TypeError):
        list_to_decimal(typerr)


@pytest.mark.parametrize(
    "valerr",
    [
        [-1, 12],
        [33, 22],
        [10],
    ],
)
def test_raise_value_errors(valerr):
    with pytest.raises(ValueError):
        list_to_decimal(valerr)


@pytest.mark.parametrize(
    "lst, result",
    [
        ([0, 4, 2, 8], 428),
        ([1, 2], 12),
        ([3], 3),
    ],
)
def test_three_dig(lst, result):
    assert list_to_decimal(lst) == result
