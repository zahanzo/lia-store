import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from browser_control.browser_state import _send_command

def execute(arguments: dict, context: dict) -> str:
    try:
        elements = _send_command("snapshot", {})
        if not elements:
            return "[DIRECT][EN]No clickable elements found.[/EN][PT]Nenhum elemento clicável encontrado.[/PT]"
        snapshot = "\n".join([f'- "{el["text"]}" -> {el["selector"]}' for el in elements])
        return f"[DIRECT][EN]Page snapshot:\n{snapshot}[/EN][PT]Snapshot da página:\n{snapshot}[/PT]"
    except Exception as e:
        return f"[DIRECT][EN]Snapshot error: {e}[/EN][PT]Erro no snapshot: {e}[/PT]"

REQUIREMENTS = ["playwright"]