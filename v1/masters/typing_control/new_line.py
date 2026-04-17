import pyautogui

def execute(arguments: dict, context: dict) -> str:
    count = arguments.get('count', 1)
    for _ in range(count):
        pyautogui.press('enter')
    return f'[DIRECT][EN]Created {count} new line(s)[/EN][PT]Criada(s) {count} nova(s) linha(s)[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]