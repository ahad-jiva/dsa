# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3  5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        self.assertEqual(postfix_eval("6 4 3 + 2 - * 6 /"), 5)

    def test_postfix_eval_06(self):
        self.assertEqual(postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +"), 18)

    def test_postfix_eval_07(self):
        with self.assertRaises(PostfixFormatException):
            postfix_eval("")

    def test_postfix_eval_08(self):
        self.assertEqual(postfix_eval("2 5.1 8.3 + +"), 15.4)

    def test_postfix_eval_09(self):
        self.assertEqual(postfix_eval("5 2 >>"), 1)

    def test_postfix_eval_10(self):
        self.assertEqual(postfix_eval("5 2 <<"), 20)

    def test_postfix_eval_11(self):
        with self.assertRaises(ValueError):
            postfix_eval("3 2 2 - /")

    def test_postfix_eval_12(self):
        with self.assertRaises(PostfixFormatException):
            postfix_eval("1.0 2 >>")

    def test_postfix_eval_13(self):
        with self.assertRaises(PostfixFormatException):
            postfix_eval("3 5.1 <<")

    def test_postfix_eval_14(self):
        self.assertEqual(postfix_eval("3 2 **"), 9)

    def test_postfix_eval_15(self):
        self.assertEqual(postfix_eval("-1.1 2.1 -"), -3.2)

    def test_postfix_eval_16(self):
        self.assertEqual(postfix_eval("2 -3 **"), 0.125)

    def test_postfix_eval_17(self):
        self.assertAlmostEqual(postfix_eval("3 7 /"), 0.4285714286)

    def test_prefix_eval_18(self):
        self.assertAlmostEqual(postfix_eval("38 1.2 * 3.6 2.8 / + 6 - 3.7 ** 2 / 5 / 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +"), 83442.42761745711)

    def test_postfix_eval_19(self):
        with self.assertRaises(PostfixFormatException):
            postfix_eval("5 bruh")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix("5 + 4 * 2"), "5 4 2 * +")
        self.assertEqual(infix_to_postfix("1 + 2 * 3 / 4"), "1 2 3 * 4 / +")

    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix("5 * ( 6 + 3 - 7 * 3 + 2 ) / 6"), "5 6 3 + 7 3 * - 2 + * 6 /")
        self.assertEqual(infix_to_postfix("8 + 3 * 4 + ( 6 - 2 + 2 * ( 6 / 3 - 1 ) - 3 )"),
                         "8 3 4 * + 6 2 - 2 6 3 / 1 - * + 3 - +")

    def test_infix_to_postfix_04(self):
        self.assertEqual(infix_to_postfix("-5 + 4 * -2"), "-5 4 -2 * +")
        self.assertEqual(infix_to_postfix("-1.5 + 2 * -3.1 / 4"), "-1.5 2 -3.1 * 4 / +")

    def test_infix_to_postfix_05(self):
        self.assertEqual(infix_to_postfix("3 ** 2"), "3 2 **")

    def test_infix_to_postfix_06(self):
        self.assertEqual(infix_to_postfix("3 ** 2 + 2"), "3 2 ** 2 +")

    def test_prefix_to_postfix_1(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("* + 1 2 - 3 4"), "1 2 + 3 4 - *")

    def test_prefix_to_postfix_2(self):
        self.assertEqual(prefix_to_postfix("+ + 2 * 3 4 5"), "2 3 4 * + 5 +")

    def test_prefix_to_postfix_3(self):
        self.assertEqual(prefix_to_postfix("+ + 12 * 3 -4 5.0"), "12 3 -4 * + 5.0 +")
        self.assertEqual(prefix_to_postfix("* - -3.5 / 2.3 -1.6 - / 4 5.5 -6"), "-3.5 2.3 -1.6 / - 4 5.5 / -6 - *")


if __name__ == "__main__":
    unittest.main()
