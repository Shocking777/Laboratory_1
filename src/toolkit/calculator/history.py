import json
from pathlib import Path

HISTORY_PATH = Path(__file__).parent / "history.json"


with open(HISTORY_PATH, "r", encoding="utf-8") as file:
    history = json.load(file)

def save(task: str, result: int) -> None:
    """
    Записывает выражение и результат его вычисления в историю.
    Args:
        task (str): Исходное математическое выражение.
        result (Decimal): Результат вычисления выражения.
    """
    history.append({
        "expression": task,
        "result": str(result),
    })
    with open(HISTORY_PATH, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)
