import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from browser_control.browser_state import _send_command

def execute(arguments: dict, context: dict) -> str:
    try:
        _send_command("back", {})
        return "[DIRECT][EN]Went back[/EN][PT]Voltou[/PT]"
    except Exception as e:
        return f"[DIRECT][EN]Back error: {e}[/EN][PT]Erro ao voltar: {e}[/PT]"

REQUIREMENTS = ["playwright"]