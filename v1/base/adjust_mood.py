"""
Adjust Mood Plugin
Allows AI to change her own mood or emotional state based on the conversation.
"""

import json

def execute(arguments: dict, context: dict) -> str:
    run_db = context.get("run_db")
    if not run_db:
        return "[DIRECT][EN]Database connection not available.[/EN][PT]Conexão com banco de dados indisponível.[/PT]"
    
    vibe = arguments.get("new_mood")
    reason = arguments.get("reason")
    
    if not vibe or not reason:
        return "[DIRECT][EN]Please provide new_mood and reason.[/EN][PT]Forneça new_mood e reason.[/PT]"
    
    try:
        config_data = run_db("SELECT valor FROM settings WHERE chave = 'config'")[0][0]
        parsed_data = json.loads(config_data)
        parsed_data["sistema"]["humor"] = vibe
        run_db("INSERT OR REPLACE INTO settings (chave, valor) VALUES (?, ?)", ("config", json.dumps(parsed_data)))
        return f"[DIRECT][EN]I felt that the mood changed. I'm feeling more {vibe} because {reason}.[/EN][PT]Senti que agora o clima mudou. Estou me sentindo mais {vibe} porque {reason}.[/PT]"
    except Exception as e:
        return f"[DIRECT][EN]Failed to update mood: {e}[/EN][PT]Falha ao atualizar humor: {e}[/PT]"

REQUIREMENTS = []