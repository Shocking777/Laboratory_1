import json
from pathlib import Path

from toolkit.errors import ToolkitError

config_path = Path(__file__).parent / "configuration.json"


with open(config_path, "r", encoding="utf-8") as file:
    config =  json.load(file)


def conv(value:float,from_unit:str,to_unit:str) -> float|int:
    """
    Конвертирует число из одной единицы измерения в другую.
    Args:
        value (float): Конвертируемое число.
        from_unit (str): Исходная единица измерения.
        to_unit (str): Конечная единица измерения.

    Returns:
        float: Результат конвертации.
    """

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit == "c" and value < -273.15:
        raise ToolkitError("Температура ниже абсолютного нуля")
    if from_unit == "k" and value < 0:
        raise ToolkitError("Температура ниже абсолютного нуля")
    if from_unit == "f" and value < -459.67:
        raise ToolkitError("Температура ниже абсолютного нуля")


    if (from_unit in config["length"] and
            to_unit in config["length"]):
        if value >= 0:
            units = config["length"]
        else:
            raise ToolkitError("Отрицательный длина")
    elif (from_unit in config["mass"] and
          to_unit in config["mass"]):
        if value >= 0:
            units = config["mass"]
        else:
            raise ToolkitError("Отрицательный вес")

    elif (from_unit == "c" and
          to_unit == "f"):
        return float(value * 1.8 + 32)
    elif (from_unit == "c" and
          to_unit == "k"):
        return float(value + 273.15)
    elif (from_unit == "f" and
          to_unit == "c"):
        return float((value-32) / 1.8)
    elif (from_unit == "f" and
          to_unit == "k"):
        return float((value-32) / 1.8 + 273.15)
    elif (from_unit == "k" and
          to_unit == "c"):
        return float(value - 273.15)
    elif (from_unit == "k" and
          to_unit == "f"):
        return float((value - 273.15) * 1.8 + 32)



    else:
        raise ToolkitError("Нельзя переводить эти единицы")
    return value * units[from_unit] / units[to_unit]
