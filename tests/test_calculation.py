from decimal import Decimal

import pytest
from typer.testing import CliRunner

from toolkit.__main__ import app
from toolkit.calculator.calculator_main import calc
from toolkit.errors import ToolkitError


def test_add():
    assert calc("2+3") == 5


def test_subtract():
    assert calc("10 - 4") == 6


def test_multiply():
    assert calc("3 * 4") == 12


def test_divide():
    assert calc("10 / 2") == 5


def test_priority():
    assert calc("2 + 3 * 4") == 14


##def test_parentheses():
    ##assert calc("(2 + 3) * 4") == 20


def test_unary_minus():
    assert calc("-5 + 2") == -3


def test_float_numbers():
    assert calc("5.2 * 3") == Decimal("15.6")


def test_two_minus_minus_two():
    assert calc("2--2") == 4


def test_modulo():
    assert calc("10 % 3") == 1


def test_floor_division():
    assert calc("10 // 3") == 3


def test_invalid_character():
    with pytest.raises(ToolkitError):
        calc("2 + a")


def test_two_binary_operators():
    with pytest.raises(ToolkitError):
        calc("2 * / 3")


def test_missing_operand():
    with pytest.raises(ToolkitError):
        calc("2 +")


def test_division_by_zero():
    with pytest.raises(ToolkitError):
        calc("10 / 0")


def test_empty_expression():
    with pytest.raises(ToolkitError):
        calc("")


def test_floor_division_by_zero():
    with pytest.raises(ToolkitError):
        calc("10 // 0")


def test_modulo_by_zero():
    with pytest.raises(ToolkitError):
        calc("10 % 0")


runner = CliRunner()
def test_cli_calc_success():
    result = runner.invoke(app, ["calc", "2 + 2 * 2"])
    assert result.exit_code == 0
    assert result.stderr == ""
    assert result.stdout.strip() == "6"


def test_cli_calc_empty_expression_fails():
    result = runner.invoke(app, ["calc", ""])
    assert result.exit_code == 2
    assert result.stdout == ""
    assert "Пустое выражение" in result.stderr
