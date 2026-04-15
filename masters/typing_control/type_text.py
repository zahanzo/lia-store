import pyautogui

def execute(arguments: dict, context: dict) -> str:
    text = arguments.get('text', '')
    pyautogui.write(text, interval=0.03)
    return f'[DIRECT][EN]Typed: {text}[/EN][PT]Digitado: {text}[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]