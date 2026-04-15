import pyautogui

def execute(arguments: dict, context: dict) -> str:
    pyautogui.hotkey('ctrl', 'a')
    return '[DIRECT][EN]Selected all text[/EN][PT]Todo o texto selecionado[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]