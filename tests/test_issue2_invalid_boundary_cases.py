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


class TestIssue2InvalidBoundaryCases(unittest.TestCase):
    def test_rectangle_perimeter_invalid_negative(self):
        with self.assertRaises(ValueError):
            rectangle_perimeter(-1, 3)

    def test_rectangle_area_boundary_zero(self):
        with self.assertRaises(ValueError):
            rectangle_area(0, 3)

    def test_solve_quadratic_invalid_a_zero(self):
        with self.assertRaises(ValueError):
            solve_quadratic(0, 2, 1)

    def test_solve_quadratic_no_real_root(self):
        result = solve_quadratic(1, 0, 1)
        self.assertEqual(result["type"], "no_real_root")
        self.assertEqual(result["roots"], ())

    def test_days_in_month_boundary_month_0(self):
        with self.assertRaises(ValueError):
            days_in_month(0, 2024)

    def test_days_in_month_boundary_month_13(self):
        with self.assertRaises(ValueError):
            days_in_month(13, 2024)

    def test_days_in_month_invalid_type(self):
        with self.assertRaises(TypeError):
            days_in_month("2", 2024)

    def test_is_prime_boundary_1(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_invalid_type(self):
        with self.assertRaises(TypeError):
            is_prime(3.5)

    def test_alternating_sum_boundary_zero(self):
        with self.assertRaises(ValueError):
            alternating_sum(0)

    def test_gcd_invalid_both_zero(self):
        with self.assertRaises(ValueError):
            gcd(0, 0)

    def test_gcd_invalid_type(self):
        with self.assertRaises(TypeError):
            gcd(5, "10")

    def test_sum_factorials_boundary_zero(self):
        with self.assertRaises(ValueError):
            sum_factorials(0)

    def test_sum_factorials_invalid_type(self):
        with self.assertRaises(TypeError):
            sum_factorials(2.2)


if __name__ == "__main__":
    unittest.main()
