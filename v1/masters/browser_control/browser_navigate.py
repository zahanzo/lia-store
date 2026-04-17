"""
Browser Navigate Tool
"""

import sys
import os
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from browser_control.browser_state import _send_command

def execute(arguments: dict, context: dict) -> str:
    url = arguments.get("url", "").strip()
    if not url:
        return "[DIRECT][EN]Please provide a URL.[/EN][PT]Forneça uma URL.[/PT]"
    
    # Adiciona https:// se nenhum protocolo for especificado
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    
    try:
        msg = _send_command("navigate", {"url": url})
        snapshot = _send_command("snapshot", {})
        snapshot_str = json.dumps(snapshot, ensure_ascii=False)
        system_tag = f"[SYSTEM]{snapshot_str}[/SYSTEM]"

        return f"[DIRECT][EN]Navigated to {url}[/EN][PT]Navegou para {url}[/PT]{system_tag}"
    except Exception as e:
        return f"[DIRECT][EN]Navigation error: {e}[/EN][PT]Erro de navegação: {e}[/PT]"

REQUIREMENTS = ["playwright"]