import pyautogui

def execute(arguments: dict, context: dict) -> str:
    count = arguments.get('count', 1)
    for _ in range(count):
        pyautogui.press('tab')
    return f'[DIRECT][EN]Pressed Tab {count} time(s)[/EN][PT]Pressionado Tab {count} vez(es)[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]