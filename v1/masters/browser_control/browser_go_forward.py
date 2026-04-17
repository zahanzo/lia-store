import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from browser_control.browser_state import _send_command

def execute(arguments: dict, context: dict) -> str:
    try:
        _send_command("forward", {})
        return "[DIRECT][EN]Went forward[/EN][PT]Avançou[/PT]"
    except Exception as e:
        return f"[DIRECT][EN]Forward error: {e}[/EN][PT]Erro ao avançar: {e}[/PT]"

REQUIREMENTS = ["playwright"]