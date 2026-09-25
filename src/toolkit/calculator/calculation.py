from decimal import Decimal

from toolkit.calculator.tokenization import cif
from toolkit.errors import ToolkitError


def calculate(rpn: list) -> int|Decimal:
    """
    Вычисляет результат математического выражения в Обратной польской нотации.
    Args:
        rpn(list): Список токенов в Обратной польской нотации.

    Returns:
        int: Результат вычисления.
    """
    stack = []
    for token in rpn:
        if cif(token):
            stack.append(token)
        else:
            num_2 = Decimal(stack.pop())
            num_1 = Decimal(stack.pop())

            if token == "+":
                stack.append(num_1 + num_2)
            elif token == "-":
                stack.append(num_1 - num_2)
            elif token == "*":
                stack.append(num_1 * num_2)
            elif token == "/":
                if int(num_2) == 0:
                    raise ToolkitError("Деление на ноль")
                stack.append(num_1 / num_2)
            elif token == "%":
                if int(num_2) == 0:
                    raise ToolkitError("Деление на ноль")
                stack.append(num_1 % num_2)
            elif token == "@":
                if int(num_2) == 0:
                    raise ToolkitError("Деление на ноль")
                stack.append(num_1 // num_2)

    return stack[0]
