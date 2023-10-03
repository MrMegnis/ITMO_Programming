from collections import deque


class ExpressionError(Exception):
    pass


class Calculator:
    def __init__(self):
        self.symbols_allowed = "1234567890()+-*/ "

    def is_corr_brack_seq(self, seq: str) -> bool:
        stack = deque()
        for i in seq:
            if i in "()":
                if i == ")":
                    if len(stack) == 0:
                        return False
                    top = stack[-1]
                    if top == "(":
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(i)
        return len(stack) == 0

    def is_expression_correct(self, expression: str) -> bool:
        is_digit_in_exp = False
        for i in expression:
            if i not in self.symbols_allowed:
                return False
            if i.isdigit():
                is_digit_in_exp = True
        return is_digit_in_exp and self.is_corr_brack_seq(expression)

    def calc(self, expression: str):
        if not self.is_expression_correct(expression):
            # raise ExpressionError
            return "Expression is not correct"
        return eval(expression)


def main():
    calculator = Calculator()
    inp = input().strip()
    while inp != "":
        print(calculator.calc(inp.strip()))
        inp = input()


if __name__ == "__main__":
    main()
