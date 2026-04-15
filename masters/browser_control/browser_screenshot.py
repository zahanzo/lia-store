import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from browser_control.browser_state import _send_command

def execute(arguments: dict, context: dict) -> str:
    path = arguments.get("path", "screenshot.png")
    try:
        _send_command("screenshot", {"path": path})
        return f"[DIRECT][EN]Screenshot saved to {path}[/EN][PT]Captura salva em {path}[/PT]"
    except Exception as e:
        return f"[DIRECT][EN]Screenshot error: {e}[/EN][PT]Erro na captura: {e}[/PT]"

REQUIREMENTS = ["playwright"]