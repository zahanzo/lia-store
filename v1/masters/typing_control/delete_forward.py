import pyautogui

def execute(arguments: dict, context: dict) -> str:
    count = arguments.get('count', 1)
    for _ in range(count):
        pyautogui.press('delete')
    return f'[DIRECT][EN]Deleted {count} character(s) forward[/EN][PT]Apagado {count} caractere(s) para a frente[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]