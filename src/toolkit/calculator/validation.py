from toolkit.calculator.tokenization import cif
from toolkit.constants import ADDITIVE_OPERATORS, MULTIPLICATIVE_OPERATORS
from toolkit.errors import ToolkitError


def validate_input(exp: str) -> None:
    """
    Проверяет исходное математическое выражение на наличии ошибок
    Args:
        exp(str): Исходное математическое выражение.

    """
    if not exp.strip():
        raise ToolkitError("Пустое выражение")
    for i in exp:
        if i not in ADDITIVE_OPERATORS+MULTIPLICATIVE_OPERATORS+"0123456789"+"()"+" "+".":
            raise ToolkitError("Недопустимый символ")

    tokens = exp.split()

    for index in range(len(tokens) - 1):
        if (tokens[index] in ADDITIVE_OPERATORS + MULTIPLICATIVE_OPERATORS and
            tokens[index + 1] in ADDITIVE_OPERATORS + MULTIPLICATIVE_OPERATORS and
            tokens[index] not in "+-" and
            tokens[index + 1] not in "+-"):
            raise ToolkitError("Два бинарных оператора подряд")


def validate_rpn(rpn: list) -> None:
    """
    Проверяет список токенов в Обратной польской нотации на наличие ошибок.
    Args:
        rpn(list): Список токенов в Обратной польской нотации.

    """
    numbers = 0
    operators = 0
    for i in rpn:
        if cif(i):
            numbers += 1
        if i in ADDITIVE_OPERATORS + MULTIPLICATIVE_OPERATORS:
            operators += 1
    if numbers - operators != 1:
        raise ToolkitError("Пропущенный операнд")
