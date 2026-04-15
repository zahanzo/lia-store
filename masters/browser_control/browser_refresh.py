import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from browser_control.browser_state import _send_command

def execute(arguments: dict, context: dict) -> str:
    try:
        _send_command("refresh", {})
        return "[DIRECT][EN]Page refreshed[/EN][PT]Página recarregada[/PT]"
    except Exception as e:
        return f"[DIRECT][EN]Refresh error: {e}[/EN][PT]Erro ao recarregar: {e}[/PT]"

REQUIREMENTS = ["playwright"]