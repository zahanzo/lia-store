"""
Open App Plugin
Opens programs and files on the local computer.
"""

import os

def execute(arguments: dict, context: dict) -> str:
    app_name = arguments.get("app_name", "").strip().lower()
    if not app_name:
        return "[DIRECT][EN]Please provide an application name.[/EN][PT]Forneça o nome de um aplicativo.[/PT]"
    
    shortcuts = {
        "bloco de notas": "notepad.exe", "notepad": "notepad.exe",
        "calculadora": "calc.exe", "calculator": "calc.exe",
        "vscode": "code"
    }
    
    if app_name in shortcuts:
        os.startfile(shortcuts[app_name])
        return f"[DIRECT][EN]Done! I've opened {app_name} for you.[/EN][PT]Pronto! Já abri o {app_name} para você.[/PT]"
    else:
        return f"[DIRECT][EN]Oops, I don't have the shortcut for '{app_name}' yet.[/EN][PT]Poxa, eu ainda não tenho o atalho para o '{app_name}'.[/PT]"

REQUIREMENTS = []