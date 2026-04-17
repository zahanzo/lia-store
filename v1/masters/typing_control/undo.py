import pyautogui

def execute(arguments: dict, context: dict) -> str:
    count = arguments.get('count', 1)
    for _ in range(count):
        pyautogui.hotkey('ctrl', 'z')
    return f'[DIRECT][EN]Undone {count} action(s)[/EN][PT]Desfeita {count} ação(ões)[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]