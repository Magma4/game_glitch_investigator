from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_score_decrease_on_miss():
    # Score should decrease by 5 on a miss
    initial_score = 100
    new_score = update_score(initial_score, "Too High", 1)
    assert new_score == 95

# --- Challenge 1: Edge Case Tests ---

from logic_utils import parse_guess

def test_parse_decimal():
    # Decimals should be truncated to integers
    ok, val, err = parse_guess("50.9")
    assert ok is True
    assert val == 50

def test_parse_extremely_large():
    # Extremely large numbers should be rejected
    ok, val, err = parse_guess("9999999999")
    assert ok is False
    assert "too large" in err.lower()

def test_parse_invalid_string():
    # Non-numeric strings should be rejected
    ok, val, err = parse_guess("abc")
    assert ok is False
    assert "not a valid number" in err.lower()

def test_parse_empty():
    # Empty strings should be rejected
    ok, val, err = parse_guess("   ")
    assert ok is False
    assert "enter a guess" in err.lower()
