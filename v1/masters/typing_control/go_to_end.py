import pyautogui

def execute(arguments: dict, context: dict) -> str:
    pyautogui.press('end')
    return '[DIRECT][EN]Moved to end of line[/EN][PT]Movido para o fim da linha[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]