import unittest

from src.algorithms import (
    alternating_sum,
    days_in_month,
    gcd,
    is_prime,
    rectangle_area,
    rectangle_perimeter,
    solve_quadratic,
    sum_factorials,
)


class TestIssue1ValidCases(unittest.TestCase):
    def test_rectangle_perimeter_valid(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16)

    def test_rectangle_area_valid(self):
        self.assertEqual(rectangle_area(5, 3), 15)

    def test_solve_quadratic_two_roots(self):
        result = solve_quadratic(1, -3, 2)
        self.assertEqual(result["type"], "two_roots")
        self.assertEqual(set(result["roots"]), {1.0, 2.0})

    def test_solve_quadratic_double_root(self):
        result = solve_quadratic(1, 2, 1)
        self.assertEqual(result["type"], "double_root")
        self.assertEqual(result["roots"], (-1.0,))

    def test_days_in_month_31_days(self):
        self.assertEqual(days_in_month(1, 2024), 31)

    def test_days_in_month_feb_leap_year(self):
        self.assertEqual(days_in_month(2, 2024), 29)

    def test_days_in_month_feb_non_leap_year(self):
        self.assertEqual(days_in_month(2, 2023), 28)

    def test_is_prime_true(self):
        self.assertTrue(is_prime(13))

    def test_is_prime_false(self):
        self.assertFalse(is_prime(15))

    def test_alternating_sum_valid(self):
        # S = 1 - 2 + 3 - 4 + 5 = 3
        self.assertEqual(alternating_sum(5), 3)

    def test_gcd_valid(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_gcd_with_zero(self):
        self.assertEqual(gcd(0, 5), 5)

    def test_sum_factorials_valid(self):
        # 1! + 2! + 3! = 1 + 2 + 6 = 9
        self.assertEqual(sum_factorials(3), 9)


if __name__ == "__main__":
    unittest.main()
