# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game was functional but riddled with logical errors and "glitches" that made the experience confusing and frustrating.

- **Bug 1: Lying Hints**
  - **What I expected:** If my guess is "Too High", the hint should tell me to go "Lower".
  - **What happened:** The code returns "📈 Go HIGHER!" when the guess is > secret, and vice-versa, making the hints actively misleading.
- **Bug 2: Haywire Scoring**
  - **What I expected:** The score should decrease or stay the same when making an incorrect guess.
  - **What happened:** On even attempt numbers, if the guess is "Too High", the player is inexplicably awarded 5 points, rewarding them for failure.
- **Bug 3: Difficulty Range Inconsistency**
  - **What I expected:** "Hard" difficulty should offer a more challenging (larger) range of numbers to guess from.
  - **What happened:** The "Hard" difficulty range is set to 1-50, which is actually smaller and easier than "Normal" (1-100), defeating the purpose of the setting.
- **Bug 4: Secret Identity Crisis**
  - **What I expected:** The secret number should remain an integer for consistent comparison.
  - **What happened:** On even-numbered attempts, the secret is converted to a string before comparison, leading to messy type-mismatch handling in the logic.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Antigravity, which is powered by Google's Gemini models, as my primary pair programmer and agent.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - The AI suggested refactoring all game logic into `logic_utils.py` and provided the correct logic for `get_range_for_difficulty`. I verified this by running `pytest` and checking the range values in the Streamlit sidebar after switching to "Hard" mode.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - The AI initially generated a `pytest` case that failed because it expected `check_guess` to return a string, while the refactored function actually returns a tuple `(outcome, message)`. I verified this by observing the `AssertionError` in the terminal and then corrected the test case to match the new return signature.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - A bug was considered fixed when both the automated `pytest` cases passed and the manual behavior in the Streamlit app matched user expectations (e.g., correct hints, proper scoring decrease).
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  - I ran a `pytest` called `test_score_decrease_on_miss` which verified that the score consistently decreases by 5 points after an incorrect guess. This proved that the "Haywire Scoring" logic (which previously awarded points on even attempts) was successfully removed.
- Did AI help you design or understand any tests? How?
  - Yes, the AI helped generate the structure for `test_game_logic.py` and helped me diagnose why the tests were initially failing due to the tuple return type mismatch.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - I'd explain that Streamlit is like a flipbook that redraws itself from the top every time you interact with it (a "rerun"). To remember things between those redraws—like your current score or the secret number—you have to use "Session State," which acts like a small sticky note that stays stuck to the page even when it's flipped.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - The habit of "targeting the crime scene" with `# FIXME` comments before starting a refactor or fix. It creates a concrete anchor for the AI and me to focus on, preventing "scroll-fatigue" and keeping the context clear.
- What is one thing you would do differently next time you work with AI on a coding task?
  - I would be more proactive about defining the return types and interfaces for refactored functions *before* the AI starts writing the code. This would prevent the "assertion mismatch" issues I had with `pytest` where the AI assumed a different return format than what was implemented.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project reinforced that AI-generated code is often "syntactically perfect but logically broken." It underscored that the developer's role is no longer just writing code, but acting as a high-level auditor and investigator who must verify every logical branch.
