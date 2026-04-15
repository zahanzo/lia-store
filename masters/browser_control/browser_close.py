import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from browser_control.browser_state import _send_command

def execute(arguments: dict, context: dict) -> str:
    try:
        _send_command("close", {})
        return "[DIRECT][EN]Browser closed[/EN][PT]Navegador fechado[/PT]"
    except Exception as e:
        return f"[DIRECT][EN]Close error: {e}[/EN][PT]Erro ao fechar: {e}[/PT]"

REQUIREMENTS = ["playwright"]