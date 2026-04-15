import pyautogui

def execute(arguments: dict, context: dict) -> str:
    pyautogui.press('home')
    return '[DIRECT][EN]Moved to start of line[/EN][PT]Movido para o início da linha[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]