import pyautogui

def execute(arguments: dict, context: dict) -> str:
    count = arguments.get('count', 1)
    for _ in range(count):
        pyautogui.hotkey('ctrl', 'backspace')
    return f'[DIRECT][EN]Deleted {count} word(s)[/EN][PT]Apagada(s) {count} palavra(s)[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]