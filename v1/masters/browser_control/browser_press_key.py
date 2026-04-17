import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from browser_control.browser_state import _send_command

def execute(arguments: dict, context: dict) -> str:
    key = arguments.get("key")
    if not key:
        return "[DIRECT][EN]Please provide a key.[/EN][PT]Forneça uma tecla.[/PT]"
    try:
        _send_command("press_key", {"key": key})
        return f"[DIRECT][EN]Pressed {key}[/EN][PT]Pressionou {key}[/PT]"
    except Exception as e:
        return f"[DIRECT][EN]Press key error: {e}[/EN][PT]Erro ao pressionar tecla: {e}[/PT]"

REQUIREMENTS = ["playwright"]