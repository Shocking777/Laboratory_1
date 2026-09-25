from decimal import Decimal, InvalidOperation

from toolkit.constants import ADDITIVE_OPERATORS, MULTIPLICATIVE_OPERATORS


def cif(token: str) -> bool:
    """
    Проверяет является ли строка числом.
    Args:
        token(str): Исходная строка.

    Returns:
        bool:True , если строка является числом, иначе False.
    """
    try:
        Decimal(token)
        return True
    except InvalidOperation:
        return False


def tokenize(exp: str) -> list  :
    """
    Преобразует математическое выражение в Обратную польскую нотацию.
    Args:
        exp(str): Исходное математическое выражение.

    Returns:
        list: Список токенов в Обратной польской нотации.
    """
    oper_stack: list[str] = []
    rpn = []

    exp = exp.replace("//","@")
    exp = exp.replace(" ", "")

    exp_copy = ""
    while exp_copy != exp:
        exp_copy = exp
        exp = exp.replace("--","+")
        exp = exp.replace("-+", "-")
        exp = exp.replace("+-", "-")
        exp = exp.replace("++", "+")

    new_exp = ""
    previous = ""
    for i in range(len(exp)):
        if exp[i] == "-":
            if (previous in ADDITIVE_OPERATORS + MULTIPLICATIVE_OPERATORS or
                previous == "" or previous == "("):
                new_exp += " -"
            else:
                new_exp += " - "
        else:
            new_exp += exp[i]

        if exp[i] != " ":
            previous = exp[i]
    exp = new_exp

    new_exp = ""
    previous = ""
    for i in range(len(exp)):
        if exp[i] == "+":
            if (previous == "" or
                previous in ADDITIVE_OPERATORS + MULTIPLICATIVE_OPERATORS or
                previous == "("):
                new_exp += " +"
            else:
                new_exp += " + "
        else:
            new_exp += exp[i]

        if exp[i] != " ":
            previous = exp[i]
    exp = new_exp

    exp = exp.replace("(", " ( ")
    exp = exp.replace(")", " ) ")
    exp = exp.replace("(+", "(")

    for operator in ADDITIVE_OPERATORS+MULTIPLICATIVE_OPERATORS:
        if operator != "-" and operator != "+":
            exp = exp.replace(operator," " + operator + " ")

    for token in exp.split():
        if cif(token):
            rpn.append(token)
        if token in ADDITIVE_OPERATORS:
            while (len(oper_stack) > 0 and
                   oper_stack[-1] != "("):
                rpn.append(oper_stack.pop())
            oper_stack.append(token)
        elif token in MULTIPLICATIVE_OPERATORS:
            if (len(oper_stack) == 0 or
                oper_stack[-1] == "(" or
                oper_stack[-1] in ADDITIVE_OPERATORS):
                oper_stack.append(token)
            else:
                while (len(oper_stack) > 0 and
                        oper_stack[-1] in MULTIPLICATIVE_OPERATORS):
                    rpn.append(oper_stack.pop())
                oper_stack.append(token)

    while len(oper_stack) > 0:
        rpn.append(oper_stack.pop())

    rpn = [x for x in rpn if x != ""]
    return rpn
