import pyautogui

def execute(arguments: dict, context: dict) -> str:
    pyautogui.hotkey('ctrl', 'c')
    return '[DIRECT][EN]Copied text to clipboard[/EN][PT]Texto copiado para a área de transferência[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]