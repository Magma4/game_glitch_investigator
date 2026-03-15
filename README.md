# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- **Game Purpose**: A numbers-based guessing game where players must guess a secret number within a limited number of attempts based on selected difficulty.
- **Bugs Found**:
  - **Lying Hints**: Higher/Lower hints were reversed.
  - **Haywire Scoring**: Wrong guesses awarded points on even attempts.
  - **Range Glitches**: "Hard" mode was actually easier (smaller range) than "Normal".
  - **State Memory**: History and scores didn't clear correctly on new games.
- **Fixes Applied**:
  - Refactored core logic into a separate `logic_utils.py` module for testability.
  - Corrected conditional logic for hints and scoring penalties.
  - Updated Streamlit session state management to properly reset on "New Game".
  - Fixed integer comparison logic to prevent type-mismatch errors.

## 📸 Demo

![Winning Game Screen](/Users/ray/.gemini/antigravity/brain/faa3094b-cde1-4ad9-abc1-c154d35393de/winning_screen_1773539809815.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
