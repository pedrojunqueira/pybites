from unittest.mock import patch
import builtins

import pytest

from guess import GuessGame, InvalidNumber


@pytest.fixture(scope="function")
def game():
    gg = GuessGame(secret_number=8, max_guesses=1)
    return gg


@pytest.mark.parametrize(
    "secret, _input, _output",
    [
        (8, 9, "Guess a number: \nToo high\nSorry, the number was 8\n"),
        (8, 7, "Guess a number: \nToo low\nSorry, the number was 8\n"),
        (8, 8, "Guess a number: \nYou guessed it!\n"),
        (8, 15, "Guess a number: \nToo high\nSorry, the number was 8\n"),
        (8, 0, "Guess a number: \nToo low\nSorry, the number was 8\n"),
    ],
)
def test_guess_correct(capsys, secret, _input, _output):
    gg = GuessGame(secret_number=secret, max_guesses=1)
    with patch.object(builtins, "input", lambda: _input):
        gg()
        captured = capsys.readouterr()
        assert captured.out == _output


def test_guess_no_input(capfd, game):
    game
    with patch.object(builtins, "input", side_effect=["", 8]):
        game()
        captured = capfd.readouterr()
        assert (
            captured.out
            == "Guess a number: \nEnter a number, try again\nGuess a number: \nYou guessed it!\n"
        )
        assert game.attempt == 1


def test_default():
    gg = gg = GuessGame(10)
    assert gg.max_guesses == 5


def test_validate_right():
    gg = GuessGame(10)
    r = gg._validate(10)
    assert r == 10


def test_validate_low_bound():
    gg = GuessGame(10)
    r = gg._validate(0)
    assert r == 0


def test_validate_high_bound():
    gg = GuessGame(10)
    r = gg._validate(15)
    assert r == 15


def test_validate_ValueError():
    with pytest.raises(InvalidNumber, match="Not a number"):
        gg = GuessGame(10)
        gg._validate("somthing that is not a number")


def test_validate_Negative():
    with pytest.raises(InvalidNumber, match="Negative number"):
        gg = GuessGame(10)
        gg._validate(-1)


def test_validate_HighNumber():
    with pytest.raises(InvalidNumber, match="Number too high"):
        gg = GuessGame(10)
        gg._validate(16)