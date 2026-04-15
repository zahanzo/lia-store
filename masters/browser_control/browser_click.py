import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from browser_control.browser_state import _send_command

def execute(arguments: dict, context: dict) -> str:
    text = arguments.get("text")
    selector = arguments.get("selector")
    try:
        if text:
            msg = _send_command("click_text", {"text": text})
            return f"[DIRECT][EN]Clicked on '{text}'[/EN][PT]Clicou em '{text}'[/PT]"
        elif selector:
            msg = _send_command("click_selector", {"selector": selector})
            return f"[DIRECT][EN]Clicked on '{selector}'[/EN][PT]Clicou em '{selector}'[/PT]"
        else:
            return "[DIRECT][EN]Provide text or selector.[/EN][PT]Forneça texto ou seletor.[/PT]"
    except Exception as e:
        return f"[DIRECT][EN]Click error: {e}[/EN][PT]Erro ao clicar: {e}[/PT]"

REQUIREMENTS = ["playwright"]