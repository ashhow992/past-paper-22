# Activity 5 – Evaluation

## Aim and solution
The program generates a configurable password through a text-based Python interface. The user selects length (4–128) and which of lowercase letters, uppercase letters, digits and symbols to include. It validates input, ensures each selected category is represented, fills remaining positions and securely shuffles the result.

## Strengths
- `secrets` provides cryptographically secure random selection rather than predictable pseudorandomness.
- Separate `generate_password` function makes the solution reusable and straightforward to test.
- Boundary validation prevents empty or excessively long passwords and impossible selections.
- Repeated generation is supported without restarting the program.
- Automated tests exercise valid, invalid and boundary conditions.

## Limitations
- Passwords are displayed on screen and may be visible to someone nearby.
- There is no graphical interface, clipboard integration or password strength meter.
- The program does not save passwords, which reduces storage risk but may be inconvenient.
- The implementation follows an inferred password-generator specification; it has not been checked against the repository's original resource documents.

## Improvements
Add an optional masked display or secure clipboard copy with expiry, a clearer strength estimate, accessibility checks, and a full review against the original exam brief. Consider preventing ambiguous characters when users request it, while explaining the reduction in available character space.

## Testing conclusion
Automated unit tests are included and their actual execution result is recorded in `test_results.txt`. Interactive behaviour should additionally be manually tested. The implementation should not be described as meeting every original assessment criterion until the source brief is reviewed.
