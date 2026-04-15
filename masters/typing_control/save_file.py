import pyautogui

def execute(arguments: dict, context: dict) -> str:
    pyautogui.hotkey('ctrl', 's')
    return '[DIRECT][EN]Saved file[/EN][PT]Arquivo salvo[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]