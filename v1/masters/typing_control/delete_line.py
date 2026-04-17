import pyautogui

def execute(arguments: dict, context: dict) -> str:
    pyautogui.hotkey('home')
    pyautogui.hotkey('shift', 'end')
    pyautogui.press('delete')
    return '[DIRECT][EN]Deleted current line[/EN][PT]Linha atual apagada[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]