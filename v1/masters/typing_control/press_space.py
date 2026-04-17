import pyautogui

def execute(arguments: dict, context: dict) -> str:
    count = arguments.get('count', 1)
    for _ in range(count):
        pyautogui.press('space')
    return f'[DIRECT][EN]Pressed Space {count} time(s)[/EN][PT]Pressionado Espaço {count} vez(es)[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]