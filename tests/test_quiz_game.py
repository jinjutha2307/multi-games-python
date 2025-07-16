from unittest.mock import patch
import pytest
from games.quiz_game.quiz_game import start as quiz_game_start


@pytest.fixture
def questions():
    return [
        'Which planet is known as the "Red Planet"?',
        "What is the capital city of France?",
        "Who painted the Mona Lisa?",
        "What is the largest ocean on Earth?",
        "How many continents are there in the world?",
    ]


@pytest.mark.parametrize(
    "inputs, expected_score, wrong_count",
    [
        (["a", "c", "c", "d", "c"], 5, 0),
        (["a", "b", "c", "b", "c"], 3, 2),
        (["b", "a", "a", "a", "b"], 0, 5),
        (["A", "C", "C", "D", "C"], 5, 0),
        (["a", "c", "c", "d", "c", "a", "c", "c", "d", "c"], 5, 0),
    ],
)
def test_valid_inputs(capsys, inputs, expected_score, wrong_count, questions):
    with patch("builtins.input", side_effect=inputs):
        quiz_game_start()
        captured = capsys.readouterr()

        for q in questions:
            assert q in captured.out

        assert captured.out.count("Correct!") == expected_score
        assert captured.out.count("Wrong!") == wrong_count
        assert f"Your final score is {expected_score}/5" in captured.out


@pytest.mark.parametrize(
    "inputs, expected_score, wrong_count",
    [
        (["hello", "a", "hello", "c", "c", "hello", "d", "c"], 5, 0),
        (["hello", "a", "$", "c", "testing", "c", "gg", "d", "tt", "c"], 5, 0),
        (["", "a", "", "c", "", "c", "d", "", "c"], 5, 0),
        (["  ", "a", "      ", "  c ", "", "c", "d", "", "c"], 5, 0),
        (["a" * 100, "a", "c", "c", "d", "c"], 5, 0),
        (["a a", "a", "c", "c c", "c", "d", "c"], 5, 0),
        (["ñ", "ü", "あ", "ก", "c", "c", "d", "c"], 4, 0),
    ],
)
def test_invalid_then_valid_inputs(
    capsys, inputs, expected_score, wrong_count, questions
):

    with patch("builtins.input", side_effect=inputs):

        quiz_game_start()

        captured = capsys.readouterr()
        output = captured.out

        for q in questions:
            assert q in output

        assert "Invalid option. Please choose a valid answer (a/b/c/d)." in output
        assert output.count("Correct!") == expected_score
        assert output.count("Wrong!") == wrong_count
        assert f"Your final score is {expected_score}/5" in output


def test_invalid_then_invalid(capsys, questions):
    inputs = [
        "#",
        "$",
        "eeee",
        "-",
        ".efmef,e.",
        "#",
        "$",
        "eeee",
        "-",
        ".efmef,e.",
        "#",
        "$",
        "eeee",
        "-",
        ".efmef,e.",
        "#",
        "$",
        "eeee",
        "-",
        ".efmef,e.",
        "#",
        "$",
        "eeee",
        "-",
        ".efmef,e.",
    ]

    with patch("builtins.input", side_effect=inputs):
        quiz_game_start()

        captured = capsys.readouterr()
        output = captured.out

        for q in questions:
            assert q in output
        assert "Invalid option. Please choose a valid answer (a/b/c/d)." in output
        assert "Maximum attempts reached. Moving to the next question." in output
        assert "Your final score is 0/5" in output


@pytest.mark.parametrize(
    "inputs, expected_score, wrong_count",
    [
        (["#", "$", "eeee", "-", ".efmef,e.", "c", "c", "d", "c"], 4, 0),
        (["#", "$", "eeee", "-", ".efmef,e.", "b", "c", "a", "c"], 2, 2),
    ],
)
def test_invalid_reach_max_attempts_then_valid(
    capsys, questions, inputs, expected_score, wrong_count
):

    with patch("builtins.input", side_effect=inputs):
        quiz_game_start()

        captured = capsys.readouterr()
        output = captured.out

        for q in questions:
            assert q in output
        assert "Invalid option. Please choose a valid answer (a/b/c/d)." in output
        assert "Maximum attempts reached. Moving to the next question." in output
        assert output.count("Correct!") == expected_score
        assert output.count("Wrong!") == wrong_count
        assert f"Your final score is {expected_score}/5" in output
