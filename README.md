# Velo Test Repository 🧪

This is a **honeypot** repository designed to test the **Velo Autonomous CI/CD Healing Agent**.
It contains **intentional** bugs to verify if the agent can correctly identify and repair them.

## Intentional Bugs Included:
- **Syntax Error:** Missing colon in function definition (`sub`).
- **Indentation Error:** Wrong indentation in nested code blocks (`mul`).
- **Linting Issue:** Unused imports (`import os`).

## Workflow:
1. Run `pytest` to see the failures.
2. Expect Velo (or another agent) to fix them.
3. Verify that `test_main.py` passes completely after fixes.
