import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from browser_control.browser_state import _send_command

def execute(arguments: dict, context: dict) -> str:
    selector = arguments.get("selector", "body")
    try:
        text = _send_command("get_text", {"selector": selector})
        return f"[DIRECT][EN]Text: {text}[/EN][PT]Texto: {text}[/PT]"
    except Exception as e:
        return f"[DIRECT][EN]Get text error: {e}[/EN][PT]Erro ao obter texto: {e}[/PT]"

REQUIREMENTS = ["playwright"]