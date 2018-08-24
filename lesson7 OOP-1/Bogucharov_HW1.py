class Calculator:
    _UNARY_MINUS = '~'
    _OPEN_PAR, _CLOSED_PAR = '()'

    _operators = {'+', '-', '*', '/', '^'}
    _binop2priority = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}

    def __init__(self, tokens: list, operators: list = None):
        self._tokens = tokens
        self._operators = operators or []

    def __str__(self) -> str:
        rpn = self._make_rpn(self._tokens)
        if rpn is None:
            raise ValueError("Invalid expression")
        return ''.join(rpn).replace(Calculator._UNARY_MINUS, '-')

    def optimise(self):
        pass

    @staticmethod
    def _make_rpn(tokens: list) -> list:
        rpn = []
        op_stack = []

        prev_token = None
        for token in tokens:
            if token in Calculator._operators:  # token is an operator
                if prev_token in Calculator._operators:
                    return None

                if prev_token in (None, Calculator._OPEN_PAR):
                    op_stack.append(Calculator._UNARY_MINUS)
                else:
                    token_priority = Calculator._binop2priority[token]
                    while op_stack and op_stack[-1] != Calculator._OPEN_PAR:
                        if op_stack[-1] == Calculator._UNARY_MINUS or Calculator._binop2priority[
                            op_stack[-1]] > token_priority:
                            rpn.append(op_stack.pop())
                        else:
                            break
                    op_stack.append(token)
            elif token == Calculator._OPEN_PAR:
                op_stack.append(token)
            elif token == Calculator._CLOSED_PAR:
                while op_stack and op_stack[-1] != Calculator._OPEN_PAR:
                    rpn.append(op_stack.pop())
                if not op_stack:
                    return None
                if op_stack[-1] != Calculator._OPEN_PAR:
                    return None
                op_stack.pop()

            else:
                if token == '0' and op_stack and op_stack[-1] == '/':
                    return None
                rpn.append(token)
            prev_token = token

        if prev_token in Calculator._operators:
            return None

        while op_stack:
            token = op_stack.pop()
            if token == Calculator._OPEN_PAR:
                return None
            rpn.append(token)

        return rpn

    def validate(self) -> bool:
        rpn = self._make_rpn(self._tokens)
        return rpn is not None


validate_check_list = [
    ('a+2', True),
    ('a-(-2)', True),
    ('a+2-', False),
    ('a+(2+(3+5)', False),
    ('a^2', True),
    ('a^(-2)', True),
    ('-a-2', True),
    ('6/0', False),
    ('a/(b-b)', True),
]

str_check_list = [
    ("a", "a"),
    ("-a", "a-"),
    ("(a*(b/c)+((d-f)/k))", "abc/*df-k/+"),
    ("(a)", "a"),
    ("a*(b+c)", "abc+*"),
    ("(a*(b/c)+((d-f)/k))*(h*(g-r))", "abc/*df-k/+hgr-**"),
    ("(x*y)/(j*z)+g", "xy*jz*/g+"),
    ("a-(b+c)", "abc+-"),
    ("a/(b+c)", "abc+/"),
    ("a^(b+c)", "abc+^"),
]

for case, exp in validate_check_list:
    tokens = list(case)

    calc = Calculator(tokens).validate()
    if calc != exp:
        print(f'Error in case for "{case}". Actual "{calc}", expected {exp}')
    else:
        print(calc)

print()

for case, exp in str_check_list:
    tokens = list(case)
    calc = Calculator(tokens)
    if str(calc) != exp:
        print(f'Error in case for "{case}". Actual "{calc}", expected {exp}')
    else:
        print(calc)
