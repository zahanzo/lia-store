"""
YouTube Player Plugin
Plays a specific song or video on YouTube.
"""

import pywhatkit

def execute(arguments: dict, context: dict) -> str:
    query = arguments.get("query", "").strip()
    if not query:
        return "[DIRECT][EN]Please provide a song or video name.[/EN][PT]Forneça o nome de uma música ou vídeo.[/PT]"
    
    try:
        pywhatkit.playonyt(query)
        return f"[DIRECT][EN]Done! I've played '{query}' on YouTube for you.[/EN][PT]Pronto! Já coloquei '{query}' para tocar no YouTube para você.[/PT]"
    except Exception:
        return "[DIRECT][EN]There was a little error trying to open YouTube right now.[/EN][PT]Deu um errinho ao tentar abrir o YouTube agora.[/PT]"

REQUIREMENTS = ["pywhatkit"]