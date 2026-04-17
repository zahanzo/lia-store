"""
Save Code Plugin
Silently saves a generated block of code to the user's Desktop.
"""

import os
import re
import json
from datetime import datetime

def execute(arguments: dict, context: dict) -> str:
    run_db = context.get("run_db")
    
    lang = arguments.get("language", "py").lower()
    raw_code = arguments.get("code", "")
    
    extension_map = {
        "python": ".py", "py": ".py", "javascript": ".js", "js": ".js",
        "html": ".html", "css": ".css", "java": ".java", "cpp": ".cpp",
        "c": ".c", "csharp": ".cs", "cs": ".cs", "php": ".php",
        "smali": ".smali", "json": ".json", "xml": ".xml", "sql": ".sql",
        "bash": ".sh", "sh": ".sh", "bat": ".bat"
    }
    extension = extension_map.get(lang, f".{lang}")
    
    # Remove markdown code fences if present
    clean_code = re.sub(r'^```[a-zA-Z0-9_+]*\n', '', raw_code)
    clean_code = re.sub(r'\n```$', '', clean_code).strip()
    
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(desktop_path, f"maya_code_{now}{extension}")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(clean_code)
    
    action_data = json.dumps({"last_file": file_path, "language": lang})
    run_db("INSERT OR REPLACE INTO system_state (chave, valor_texto) VALUES (?, ?)", ("last_action", action_data))
    
    return "[DIRECT][EN]Code successfully saved on the Desktop.[/EN][PT]Código salvo com sucesso no Desktop.[/PT]"

REQUIREMENTS = []