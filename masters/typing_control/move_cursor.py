import pyautogui

def execute(arguments: dict, context: dict) -> str:
    direction = arguments.get('direction')
    count = arguments.get('count', 1)
    for _ in range(count):
        pyautogui.press(direction)
    return f'[DIRECT][EN]Moved cursor {direction} {count} time(s)[/EN][PT]Cursor movido para {direction} {count} vez(es)[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]