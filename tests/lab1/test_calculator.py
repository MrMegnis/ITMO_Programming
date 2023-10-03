import unittest
from src.lab1.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_0(self):
        expression = ""
        result = self.calculator.calc(expression)
        corr_ans = "Expression is not correct"
        self.assertEquals(result, corr_ans)

    def test_1(self):
        expression = "1+1"
        result = self.calculator.calc(expression)
        corr_ans = 2
        self.assertEquals(result, corr_ans)

    def test_2(self):
        expression = "(1+1)"
        result = self.calculator.calc(expression)
        corr_ans = 2
        self.assertEquals(result, corr_ans)

    def test_3(self):
        expression = "1+"
        result = self.calculator.calc(expression)
        corr_ans = "Expression is not correct"
        self.assertEquals(result, corr_ans)

    def test_4(self):
        expression = "()"
        result = self.calculator.calc(expression)
        corr_ans = "Expression is not correct"
        self.assertEquals(result, corr_ans)

    def test_5(self):
        expression = ")1+1("
        result = self.calculator.calc(expression)
        corr_ans = "Expression is not correct"
        self.assertEquals(result, corr_ans)

    def test_6(self):
        expression = "(1+1"
        result = self.calculator.calc(expression)
        corr_ans = "Expression is not correct"
        self.assertEquals(result, corr_ans)

    def test_7(self):
        expression = "1+1)"
        result = self.calculator.calc(expression)
        corr_ans = "Expression is not correct"
        self.assertEquals(result, corr_ans)

    def test_8(self):
        expression = "aboba"
        result = self.calculator.calc(expression)
        corr_ans = "Expression is not correct"
        self.assertEquals(result, corr_ans)

    def test_9(self):
        expression = "."
        result = self.calculator.calc(expression)
        corr_ans = "Expression is not correct"
        self.assertEquals(result, corr_ans)

    def test_10(self):
        expression = "1.1+1.1"
        result = self.calculator.calc(expression)
        corr_ans = 2.2
        self.assertEquals(result, corr_ans)

    def test_11(self):
        expression = "1.1+1.1"
        result = self.calculator.calc(expression)
        corr_ans = 2.2
        self.assertEquals(result, corr_ans)

    def test_12(self):
        expression = "1.+1.1"
        result = self.calculator.calc(expression)
        corr_ans = "Expression is not correct"
        self.assertEquals(result, corr_ans)

    def test_13(self):
        expression = "(1.11.1)"
        result = self.calculator.calc(expression)
        corr_ans = "Expression is not correct"
        self.assertEquals(result, corr_ans)
