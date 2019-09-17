from typing import List, Tuple, Any, Callable

class Operator:
    def __init__(self, symbol:str):
        self.symbol = symbol
        self.precedence, self.behavior = self.create_behavior(symbol)
    
    def __str__(self):
        return self.symbol
    
    def __repr__(self):
        return self.symbol
    
    def greater_precedence(self, op: 'Operator') -> bool:
        return self.precedence > op.precedence
    
    def operate(self, op1, op2):
        return self.behavior(op1, op2)
    
    def mult(self, op1: int, op2: int ) -> int:
        return op1 * op2

    def div(self, op1: int, op2: int ) -> int:
        return op1 / op2
    
    def add(self, op1: int, op2: int ) -> int:
        return op1 + op2
    
    def subs(self, op1: int, op2: int ) -> int:
        return op1 - op2
    
    def create_behavior(self, symbol: str) -> Tuple[int, Callable]:
        if symbol == '*':
            return 4, self.mult
        if symbol == '/':
            return 4, self.div
        if symbol == '+':
            return 3, self.add
        if symbol == '-':
            return 3, self.subs
        if symbol == '(':
            return 0, None
        if symbol == ')':
            return 0, None

    
def infix_to_postfix(exp: str) -> List[Any]:
    """ Shunting yard algorithm (E. Dijkstra).
    - Time complexity: O(n)
    - Space complexity: O(n)
    """
    exp_as_list = exp.strip().split(" ")
    postfix = []
    stack = []
    for elem in exp_as_list:
        if elem.isdigit():
            postfix.append(int(elem))
        else:
            op = Operator(elem)
            if op.symbol == ')':
                while stack[-1].symbol != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                if op.symbol != '(' and stack:
                    while stack[-1].greater_precedence(op) and stack[-1].symbol != '(':
                        postfix.append(stack.pop())
                stack.append(op)
    while stack:
        op = stack.pop()
        if op.symbol != '(':
            postfix.append(op)
    
    return postfix
    
def postfix_calculator(exp: List[Any]) -> int:
    """Postfix expressions are more computationally efficient than Infix exps.
    - Time complexity: O(n)
    - Space complexity: O(n)
    """
    stack = []
    for elem in exp:
        if type(elem) is int:
            stack.append(elem)
        else:
            result = elem.behavior(stack[-2], stack[-1])
            stack.pop()
            stack.pop()
            if stack:
                stack.append(result)
            else:
                return result

def calculate_expression(exp: str) -> int:
    return postfix_calculator(infix_to_postfix(exp))

import unittest

class Test(unittest.TestCase):
    def test_infix_to_postfix(self):
        self.assertEqual(" ".join([str(e) for e in infix_to_postfix("3 + 4")]), "3 4 +")
        self.assertEqual(" ".join([str(e) for e in infix_to_postfix("1 + 2 * 4")]), "1 2 4 * +")
        self.assertEqual(" ".join([str(e) for e in infix_to_postfix("1 + 2 * 4 - ( 6 - 2 )")]), "1 2 4 * 6 2 - - +")
        self.assertEqual(" ".join([str(e) for e in infix_to_postfix("4 * ( 1 + 2 * ( 9 / 3 ) - 5 )")]), "4 1 2 9 3 / * 5 - + *")

   
    def test_calculate_expression(self):
        self.assertEqual(calculate_expression("3 + 4"), 7)
        self.assertEqual(calculate_expression("1 + 2 * 4"), 9)
        self.assertEqual(calculate_expression("1 + 2 * 4 - ( 6 - 2 )"), 5)
        self.assertEqual(calculate_expression("4 * ( 1 + 2 * ( 9 / 3 ) - 5 )"), 8)
