import unittest
from src.functions import expr


class ConsoleCalcEasyLevelCase(unittest.TestCase):
    def test_sum_n_int_elements(self):
        res = expr("1002+10+58+687")
        self.assertEqual(res, 1757)

    def test_sum_and_sub_n_int_elements(self):
        res = expr("12-46+100-45+23")
        self.assertEqual(res, 44)

    def test_sum_n_float_elements(self):
        res = expr("3.69+8.25+98.3")
        self.assertEqual(res, 110.24)

    def test_sum_and_sub_n_float_elements(self):
        res = expr("1.2+6.8-0.33")
        self.assertEqual(res, 7.67)

    def test_mul_n_int_elements(self):
        res = expr("15*19*40*9")
        self.assertEqual(res, 102600)

    def test_mul_and_div_n_int_elements(self):
        res = expr("15/8*87")
        self.assertEqual(res, 163.125)

    def test_mul_n_float_elements(self):
        res = expr("1.5*3.9*8.55")
        self.assertEqual(res, 50.0175)

    def test_mul_and_div_n_float_elements(self):
        res = expr("1.5*3/9")
        self.assertEqual(res, 0.5)

    def test_negative_num_mul(self):
        res = expr("-1*8")
        self.assertEqual(res, -8)

    def test_mul_div_reversion(self):
        res = expr("7*9/9")
        self.assertEqual(res, 7)

    def test_zero_division_error(self):
        self.assertRaises(ZeroDivisionError, expr, "7/0")

    def test_value_error_none_string(self):
        self.assertRaises(ValueError, expr, "")

    def test_value_error_not_num_signs(self):
        self.assertRaises(ValueError, expr, "12fd+16")

    def test_complex_calc(self):
        res = expr("7*9+9*6/8+9/9-71/5*10")
        self.assertEqual(res, -71.25)
