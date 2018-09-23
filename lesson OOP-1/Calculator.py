# Склеивание элементов списка - используется для токенов, состоящих из нескольких символов
def union(l):
    i = 0
    while i < len(l):
        if l[i].isalpha():
            j = i + 1
            while (j < len(l)) and (l[j].isalpha()):
                l[i] += l[j]
                j += 1
            del l[i+1:j]
        elif l[i].isnumeric():
            j = i + 1
            while (j < len(l)) and (l[j].isnumeric()):
                l[i] += l[j]
                j += 1
            del l[i+1:j]
        i += 1
    return l

# Класс узла
class Node:
    def __init__(self, data, parent = None, left = None, right = None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def print(self, n = 0):
        if self.left:
            self.left.print(n + 1)
        if self:
            print(n, ' ', self.data)
        if self.right:
            self.right.print(n + 1)

# Базовый оптимизатор
class Optimiser:
    @staticmethod
    def pre_process(infix_expr):
        root = Node(infix_expr[-1])
        cur = root
        i = len(infix_expr) - 2
        while i >= 0:
            if infix_expr[i] in Calculator._operators:
                if cur.right == None:
                    cur.right = Node(infix_expr[i], cur, None)
                    if cur.right.data in Calculator._operators:
                        cur = cur.right
                elif cur.left == None:
                    cur.left = Node(infix_expr[i], cur, None)
                    if cur.left.data in Calculator._operators:
                        cur = cur.left
                else:
                    while (cur.left != None) and (cur.right != None):
                        cur = cur.parent
                    if cur.right == None:
                        cur.right = Node(infix_expr[i], cur, None)
                        if cur.right.data in Calculator._operators:
                            cur = cur.right
                    else:
                        cur.left = Node(infix_expr[i], cur, None)
                        if cur.left.data in Calculator._operators:
                            cur = cur.left
                i -= 1
            elif infix_expr[i] == '~':
                while (cur.left != None) and (cur.right != None):
                    cur = cur.parent
                if cur.right == None:
                    cur.right = Node(infix_expr[i], cur, None)
                    cur = cur.right
                else:
                    cur.left = Node(infix_expr[i], cur, None)
                    cur = cur.left
                i -= 1
            else:
                while (cur.left != None) and (cur.right != None):
                    cur = cur.parent
                if cur.right == None:
                    cur.right = Node(infix_expr[i], cur, None)
                    if cur.right.data in Calculator._operators:
                        cur = cur.right
                else:
                    cur.left = Node(infix_expr[i], cur, None)
                    if cur.left.data in Calculator._operators:
                        cur = cur.left
                while (cur) and (cur.data == '~'):
                    cur = cur.parent
                i -= 1
        return root

    @staticmethod
    def post_process(root, result = ''):
        if root:
            if root.left:
                result = Optimiser.post_process(root.left, result)
            if root.right:
                result = Optimiser.post_process(root.right, result)
            if root.data == '~':
                result += '-'
            else:
                result += str(root.data)
        return result

# Оптимизация двойного отрицания
class DoubleNegativeOptimiser(Optimiser):
    def process_internal(self, node):
        if node.left:
            self.process_internal(node.left)
        if node.right:
            self.process_internal(node.right)
        if node.data == '~':
            if (node.right != None) and (node.right.data == '~'):
                node.data = node.right.right.data
                node.right.right = None
                node.right = None
            elif (node.left != None) and (node.left.data == '~'):
                node.data = node.left.right.data
                node.left.right = None
                node.left = None
        elif node.data == '-':
            if (node.right != None) and (node.right.data == '~'):
                i = 1
                n = node.right
                while (n.right != None) and (n.right.data == '~'):
                    i += 1
                    n = n.right
                if i % 2 == 1:
                    node.right.data = n.right.data
                    node.right.right = None
                    node.data = '+'
                else:
                    node.right.data = n.data
                    node.right.right = None
            elif (node.left != None) and (node.left.data == '~'):
                i = 1
                n = node.left
                while (n.right != None) and (n.right.data == '~'):
                    i += 1
                    n = n.right
                if i % 2 == 0:
                    node.left.data = n.data
                    node.left.right = None
                    node.data = '+'
                else:
                    node.left.data = n.data
                    node.left.right = None

# Оптимизация констант
class IntegerConstantsOptimiser(Optimiser):
    def process_internal(self, node):
        if node.left:
            self.process_internal(node.left)
        if node.right:
            self.process_internal(node.right)
        if node.data == '+':
            if (node.left.data.isnumeric()) and (node.right.data.isnumeric()):
                node.data = str(int(node.left.data) + int(node.right.data))
                node.left = None
                node.right = None
        elif node.data == '-':
            if (node.left.data.isnumeric()) and (node.right.data.isnumeric()):
                node.data = str(int(node.left.data) - int(node.right.data))
                node.left = None
                node.right = None
        elif node.data == '*':
            if (node.left.data.isnumeric()) and (node.right.data.isnumeric()):
                node.data = str(int(node.left.data) * int(node.right.data))
                node.left = None
                node.right = None
        elif node.data == '/':
            if (node.left.data.isnumeric()) and (node.right.data.isnumeric()):
                node.data = str(int(node.left.data) // int(node.right.data))
                node.left = None
                node.right = None
        elif node.data == '^':
            if (node.left.data.isnumeric()) and (node.right.data.isnumeric()):
                node.data = str(int(node.left.data) ** int(node.right.data))
                node.left = None
                node.right = None

# Оптимизация тривиальных выражений
class SimplifierOptimiser(Optimiser):
    def process_internal(self, node):
        if node.left:
            self.process_internal(node.left)
        if node.right:
            self.process_internal(node.right)
        if node.data == '+':
            if (node.left.data == '0') and (node.right.data.isalpha()):
                node.data = node.right.data
                node.left = None
                node.right = None
            elif (node.right.data == '0') and (node.left.data.isalpha()):
                node.data = node.left.data
                node.left = None
                node.right = None
        if node.data == '-':
            if (node.right.data == '0') and (node.left.data.isalpha()):
                node.data = node.left.data
                node.left = None
                node.right = None
            elif (node.left.data == '0') and (node.right.data.isalpha()):
                node.data = '~'
                node.left = None
            elif node.left.data == node.right.data:
                node.data = '0'
                node.left = None
                node.right = None
        elif node.data == '*':
            if (node.left.data == '0') and (node.right.data.isalpha()):
                node.data = '0'
                node.left = None
                node.right = None
            elif (node.right.data == '0') and (node.left.data.isalpha()):
                node.data = '0'
                node.left = None
                node.right = None
            elif (node.left.data == '1') and (node.right.data.isalpha()):
                node.data = node.right.data
                node.left = None
                node.right = None
            elif (node.right.data == '1') and (node.left.data.isalpha()):
                node.data = node.left.data
                node.left = None
                node.right = None
        elif node.data == '/':
            if node.left.data == node.right.data:
                node.data = '1'
                node.left = None
                node.right = None
        elif node.data == '^':
            if node.right.data == '0':
                node.data = '1'
                node.left = None
                node.right = None
            elif node.right.data == '1':
                node.data = node.left.data
                node.left = None
                node.right = None

class Calculator:
    _UNARY_MINUS = '~'
    _OPEN_PAR, _CLOSED_PAR = '()'

    _operators = {'+', '-', '*', '/', '^'}
    _binop2priority = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}

    def __init__(self, tokens: list, operators: list = None, optimisers: list = None):
        self._tokens = tokens
        self._operators = operators or []
        self._optimisers = optimisers or []
        self._postfix = None

    def __str__(self) -> str:
        rpn = self._make_rpn(self._tokens)
        if rpn is None:
            if self._postfix != None:
                return self._postfix
            raise ValueError("Invalid expression")
        return ''.join(rpn).replace(Calculator._UNARY_MINUS, '-')

    def optimise(self):
        tree = Optimiser.pre_process(Calculator._make_rpn(self._tokens))
        for opt in self._optimisers:
            opt.process_internal(tree)
        self._postfix = Optimiser.post_process(tree)
        self._tokens = list(self._postfix)
        
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
    valid = Calculator(tokens).validate()
    if not valid:
        print(f'Error in case for "{case}".')
    else:
        print(case)

print()

for case, exp in str_check_list:
    tokens = list(case)
    calc = Calculator(tokens)
    if str(calc) != exp:
        print(f'Error in case for "{case}". Actual "{calc}", expected {exp}')
    else:
        print(calc)
