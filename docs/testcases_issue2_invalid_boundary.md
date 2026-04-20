# Issue 2 - Black-box test cases for invalid, boundary, exception data

This file focuses on:
- invalid equivalence classes
- out-of-range boundaries
- exception handling

## 1) Rectangle perimeter

| TC ID | Input | Technique | Expected behavior |
|---|---|---|---|
| RP-I1 | length=-1, width=3 | Invalid class | Raise ValueError |
| RP-I2 | length=0, width=3 | Boundary invalid | Raise ValueError |
| RP-I3 | length="5", width=3 | Invalid type | Raise TypeError |

## 2) Rectangle area

| TC ID | Input | Technique | Expected behavior |
|---|---|---|---|
| RA-I1 | length=0, width=3 | Boundary invalid | Raise ValueError |
| RA-I2 | length=-2, width=3 | Invalid class | Raise ValueError |

## 3) Solve quadratic equation

| TC ID | Input | Technique | Expected behavior |
|---|---|---|---|
| QE-I1 | a=0, b=2, c=1 | Invalid class | Raise ValueError |
| QE-I2 | a=1, b=0, c=1 | Valid class (delta<0) | type=no_real_root |
| QE-I3 | a="1", b=2, c=1 | Invalid type | Raise TypeError |

## 4) Number of days in month

| TC ID | Input | Technique | Expected behavior |
|---|---|---|---|
| DM-I1 | month=0, year=2024 | Boundary invalid (below 1) | Raise ValueError |
| DM-I2 | month=13, year=2024 | Boundary invalid (above 12) | Raise ValueError |
| DM-I3 | month=2, year=0 | Invalid class (year <= 0) | Raise ValueError |
| DM-I4 | month="2", year=2024 | Invalid type | Raise TypeError |

## 5) Prime check

| TC ID | Input | Technique | Expected behavior |
|---|---|---|---|
| PR-I1 | n=1 | Boundary value | False |
| PR-I2 | n=0 | Invalid domain for prime | False |
| PR-I3 | n=3.5 | Invalid type | Raise TypeError |

## 6) Alternating sum

| TC ID | Input | Technique | Expected behavior |
|---|---|---|---|
| AS-I1 | n=0 | Boundary invalid | Raise ValueError |
| AS-I2 | n=-2 | Invalid class | Raise ValueError |
| AS-I3 | n="5" | Invalid type | Raise TypeError |

## 7) GCD

| TC ID | Input | Technique | Expected behavior |
|---|---|---|---|
| GCD-I1 | a=0, b=0 | Invalid class | Raise ValueError |
| GCD-I2 | a=5, b="10" | Invalid type | Raise TypeError |

## 8) Sum of factorials

| TC ID | Input | Technique | Expected behavior |
|---|---|---|---|
| SF-I1 | n=0 | Boundary invalid | Raise ValueError |
| SF-I2 | n=-1 | Invalid class | Raise ValueError |
| SF-I3 | n=2.2 | Invalid type | Raise TypeError |
