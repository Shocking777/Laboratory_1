from decimal import Decimal

from toolkit.calculator.calculation import calculate
from toolkit.calculator.history import save
from toolkit.calculator.tokenization import tokenize
from toolkit.calculator.validation import validate_input, validate_rpn


def calc(exp: str) -> int|Decimal:
    """
    Вычисляет результат математического выражения.
    Args:
        exp(str): Исходное математическое выражение.

    Returns:
        int: Результат математического выражения.
    """
    validate_input(exp)

    rpn = tokenize(exp)

    validate_rpn(rpn)
    save(exp, int(calculate(rpn)))
    return calculate(rpn)
