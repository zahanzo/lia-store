import pyautogui

def execute(arguments: dict, context: dict) -> str:
    pyautogui.hotkey('ctrl', 'v')
    return '[DIRECT][EN]Pasted text from clipboard[/EN][PT]Texto colado da área de transferência[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]