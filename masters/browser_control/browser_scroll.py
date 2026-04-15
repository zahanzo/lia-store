import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from browser_control.browser_state import _send_command

def execute(arguments: dict, context: dict) -> str:
    direction = arguments.get("direction", "down")
    amount = arguments.get("amount", 500)
    try:
        _send_command("scroll", {"direction": direction, "amount": amount})
        return f"[DIRECT][EN]Scrolled {direction} {amount}px[/EN][PT]Rolou {direction} {amount}px[/PT]"
    except Exception as e:
        return f"[DIRECT][EN]Scroll error: {e}[/EN][PT]Erro ao rolar: {e}[/PT]"

REQUIREMENTS = ["playwright"]