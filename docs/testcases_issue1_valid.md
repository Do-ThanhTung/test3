# Issue 1 - Black-box test cases for valid data

This file contains valid-data test cases using black-box techniques:
- equivalence partitioning
- boundary value analysis (valid boundaries)

## 1) Rectangle perimeter
Input: length, width (> 0)
Output: perimeter = 2 * (length + width)

| TC ID | Input | Technique | Expected output |
|---|---|---|---|
| RP-V1 | length=5, width=3 | Valid equivalence class | 16 |
| RP-V2 | length=1, width=1 | Valid boundary (minimum positive) | 4 |

## 2) Rectangle area
Input: length, width (> 0)
Output: area = length * width

| TC ID | Input | Technique | Expected output |
|---|---|---|---|
| RA-V1 | length=5, width=3 | Valid equivalence class | 15 |
| RA-V2 | length=1, width=2 | Valid boundary | 2 |

## 3) Solve quadratic equation ax^2 + bx + c = 0
Input: a, b, c with a != 0
Output: two roots / double root / no real root

| TC ID | Input | Technique | Expected output |
|---|---|---|---|
| QE-V1 | a=1, b=-3, c=2 | Valid class (delta > 0) | type=two_roots, roots={1,2} |
| QE-V2 | a=1, b=2, c=1 | Valid boundary (delta = 0) | type=double_root, root=-1 |

## 4) Number of days in month
Input: month in [1..12], year > 0
Output: 28/29/30/31

| TC ID | Input | Technique | Expected output |
|---|---|---|---|
| DM-V1 | month=1, year=2024 | Valid class (31-day month) | 31 |
| DM-V2 | month=2, year=2024 | Valid class (leap year) | 29 |
| DM-V3 | month=2, year=2023 | Valid class (non-leap year) | 28 |
| DM-V4 | month=12, year=2024 | Valid boundary (upper month boundary) | 31 |

## 5) Prime check
Input: integer n
Output: True/False

| TC ID | Input | Technique | Expected output |
|---|---|---|---|
| PR-V1 | n=13 | Valid class (prime) | True |
| PR-V2 | n=15 | Valid class (composite) | False |
| PR-V3 | n=2 | Valid boundary (smallest prime) | True |

## 6) Alternating sum S = 1 - 2 + 3 - ... + n
Input: integer n > 0
Output: integer sum

| TC ID | Input | Technique | Expected output |
|---|---|---|---|
| AS-V1 | n=5 | Valid class | 3 |
| AS-V2 | n=1 | Valid boundary (minimum n) | 1 |

## 7) GCD of a and b
Input: integers a, b (not both zero)
Output: gcd(a,b)

| TC ID | Input | Technique | Expected output |
|---|---|---|---|
| GCD-V1 | a=48, b=18 | Valid class | 6 |
| GCD-V2 | a=0, b=5 | Valid boundary (one operand zero) | 5 |

## 8) Sum S = 1! + 2! + ... + n!
Input: integer n > 0
Output: integer sum

| TC ID | Input | Technique | Expected output |
|---|---|---|---|
| SF-V1 | n=3 | Valid class | 9 |
| SF-V2 | n=1 | Valid boundary (minimum n) | 1 |
