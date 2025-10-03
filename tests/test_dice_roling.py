from unittest.mock import patch
import pytest

from games.dice_rolling_game import start as dice_start


@pytest.mark.parametrize(
    ("inputs", "expected_dice_rolls", "fake_random"),
    [
        (["y", "1", "n"], 1, "1"),
        (["y", "2", "y", "2", "n"], 2, "[1, 2]"),
        (["y", "3", "y", "3", "y", "3", "n"], 3, " [1, 2, 3]"),
    ],
)
def test_roll_dice_then_quit(capsys, inputs, expected_dice_rolls, fake_random):

    with patch("builtins.input", side_effect=inputs), patch(
        "random.randint", return_value=fake_random
    ):

        dice_start()

        captured = capsys.readouterr()
        output = captured.out

        assert "Welcome to the Dice Rolling Game!" in output
        assert (
            "You can roll multiple dice and track how many times you've rolled them."
            in output
        )

        assert fake_random in output
        assert (
            f"Thank you!!. You have rolled the dice {expected_dice_rolls} times!!"
            in output
        )


def test_user_doesnt_roll(capsys):
    inputs = ["n"]

    with patch("builtins.input", side_effect=inputs):

        dice_start()

        capsys = capsys.readouterr()
        output = capsys.out
        assert "Welcome to the Dice Rolling Game!" in output
        assert (
            "You can roll multiple dice and track how many times you've rolled them."
            in output
        )
        assert "Thank you!!. You have rolled the dice 0 times!!" in output


@pytest.mark.parametrize(
    ("inputs", "expected_dice_rolls", "fake_random"),
    [
        # User input is invalid then valid
        (["y", "g", "y", "1", "n"], 1, "1"),
        (["y", "g", "y", "2", "y", "2", "n"], 2, "[1, 2]"),
        (["y", "g", "y", "3", "y", "3", "y", "3", "n"], 3, " [1, 2, 3]"),
        # Repeated invalid inpue"
        (["y", "#", "y", "1", "#", "n"], 1, "1"),
        (["y", "#", "y", "2", "#", "y", "#", "y", "2", "#", "n"], 2, "[1, 2]"),
        (
            [
                "y",
                "#",
                "y",
                "3",
                "#",
                "y",
                "#",
                "y",
                "3",
                "#",
                "y",
                "#",
                "y",
                "3",
                "#",
                "n",
            ],
            3,
            " [1, 2, 3]",
        ),
        (["", "y", "", "y", "3", "y", "3", "y", "3", "n"], 3, " [1, 2, 3]"),
        (["   ", "y", "     ", "y", "3", "y", "3", "y", "3", "n"], 3, " [1, 2, 3]"),
        (["y y", "y", "3", "y", "3 2 1", "y", "3", "y", "3", "n"], 3, " [1, 2, 3]"),
    ],
)
def test_invalid_then_valid(capsys, inputs, expected_dice_rolls, fake_random):

    with patch("builtins.input", side_effect=inputs), patch(
        "random.randint", return_value=fake_random
    ):

        dice_start()

        captured = capsys.readouterr()
        output = captured.out

        assert "Welcome to the Dice Rolling Game!" in output
        assert (
            "You can roll multiple dice and track how many times you've rolled them."
            in output
        )
        assert "invalid input" in output

        assert fake_random in output
        assert (
            f"Thank you!!. You have rolled the dice {expected_dice_rolls} times!!"
            in output
        )


def test_all_invalid_then_quit(capsys):
    inputs = ["#" * 100, "n"]

    with patch("builtins.input", side_effect=inputs):
        dice_start()

        captured = capsys.readouterr()
        output = captured.out

        assert "Welcome to the Dice Rolling Game!" in output
        assert (
            "You can roll multiple dice and track how many times you've rolled them."
            in output
        )
        assert "invalid input" in output
        assert "Thank you!!. You have rolled the dice 0 times!!" in output
