import pyautogui

def execute(arguments: dict, context: dict) -> str:
    count = arguments.get('count', 1)
    for _ in range(count):
        pyautogui.press('backspace')
    return f'[DIRECT][EN]Deleted {count} character(s)[/EN][PT]Apagado {count} caractere(s)[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]