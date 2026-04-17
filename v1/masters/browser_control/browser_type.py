import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from browser_control.browser_state import _send_command

def execute(arguments: dict, context: dict) -> str:
    label = arguments.get("label")
    selector = arguments.get("selector")
    text = arguments.get("text")
    press_enter = arguments.get("press_enter", False)
    
    if not text:
        return "[DIRECT][EN]Please provide text to type.[/EN][PT]Forneça o texto a digitar.[/PT]"
    
    try:
        if label:
            _send_command("type_label", {"label": label, "text": text, "press_enter": press_enter})
            return f"[DIRECT][EN]Typed '{text}' into '{label}'[/EN][PT]Digitou '{text}' em '{label}'[/PT]"
        elif selector:
            _send_command("type_selector", {"selector": selector, "text": text, "press_enter": press_enter})
            return f"[DIRECT][EN]Typed '{text}' into '{selector}'[/EN][PT]Digitou '{text}' em '{selector}'[/PT]"
        else:
            return "[DIRECT][EN]Provide label or selector.[/EN][PT]Forneça label ou seletor.[/PT]"
    except Exception as e:
        return f"[DIRECT][EN]Type error: {e}[/EN][PT]Erro ao digitar: {e}[/PT]"

REQUIREMENTS = ["playwright"]