import pyautogui

def execute(arguments: dict, context: dict) -> str:
    count = arguments.get('count', 1)
    for _ in range(count):
        pyautogui.hotkey('ctrl', 'y')
    return f'[DIRECT][EN]Redone {count} action(s)[/EN][PT]Refeita {count} ação(ões)[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]