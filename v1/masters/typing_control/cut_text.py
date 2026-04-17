import pyautogui

def execute(arguments: dict, context: dict) -> str:
    pyautogui.hotkey('ctrl', 'x')
    return '[DIRECT][EN]Cut text to clipboard[/EN][PT]Texto recortado para a área de transferência[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]