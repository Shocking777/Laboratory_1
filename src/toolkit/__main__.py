import typer

from toolkit import converter
from toolkit.calculator import calculator_main
from toolkit.errors import ToolkitError

app = typer.Typer()

@app.command(context_settings={"ignore_unknown_options": True})
def calc(expression: str):
    """
    Вычисляет математическое выражение через CLI.
    Args:
        expression(str): Исходное математическое выражение.
    """
    try:
        typer.echo(calculator_main.calc(expression))
    except ToolkitError as error:
        typer.echo(str(error),err=True)
        raise  typer.Exit(code=2)


@app.command(context_settings={"ignore_unknown_options": True})
def conv(
    value: float,
    _from_: str = typer.Option(...,"--from"),
    _to_: str = typer.Option(...,"--to")):
    """
    Конвертирует число из одной единицы измерения в другую.
    Args:
        value (float): Конвертируемое число.
        _from_(str): Иходная единица измерения.
        _to_(str): Конечная единица измерения.

    Returns:

    """
    try:
        typer.echo(converter.conv(value, _from_, _to_))
    except ToolkitError as error:
        typer.echo(str(error),err = True)
        raise  typer.Exit(code=2)
if __name__ == '__main__':
    app()
