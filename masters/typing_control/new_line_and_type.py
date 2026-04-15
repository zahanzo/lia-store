import pyautogui

def execute(arguments: dict, context: dict) -> str:
    text = arguments.get('text', '')
    pyautogui.press('enter')
    pyautogui.write(text, interval=0.03)
    return f'[DIRECT][EN]New line + typed: {text}[/EN][PT]Nova linha + digitado: {text}[/PT]'

REQUIREMENTS = ["pyautogui"]