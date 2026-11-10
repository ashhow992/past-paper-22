# Activity 3 – Test plan

| ID | Test input | Expected outcome | Type |
|---|---|---|---|
| T01 | Defaults (16, all groups) | 16 characters, all four types present | Normal |
| T02 | Length 4, all groups | Exactly four characters, one per type | Boundary |
| T03 | Length 128, all groups | Exactly 128 characters | Boundary |
| T04 | Length 3 | ValueError | Invalid boundary |
| T05 | Length 129 | ValueError | Invalid boundary |
| T06 | Length -1 | ValueError | Invalid |
| T07 | Length 0 | ValueError | Invalid |
| T08 | All categories disabled | ValueError | Invalid |
| T09 | Only digits, length 12 | Exactly 12 digits | Normal |
| T10 | Non-integer length | TypeError | Invalid |
| T11 | Two generated 32-character passwords | Usually different | Randomness smoke test |
| T12 | Interactive input `abc` for length | Error shown, user prompted again | Input handling |
| T13 | Interactive category response `maybe` | User prompted again | Input handling |
| T14 | Generate another = `n` | Program exits normally | Control flow |

Automated tests cover T01–T11. T12–T14 are interactive manual checks; do not mark them passed without executing them. Randomness tests do not prove cryptographic security; security comes from the `secrets` module.
