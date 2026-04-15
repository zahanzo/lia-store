import pyautogui
import pyperclip
import time

def execute(arguments: dict, context: dict) -> str:
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)
    text = pyperclip.paste()
    pyperclip.copy(text.upper())
    pyautogui.hotkey('ctrl', 'v')
    return '[DIRECT][EN]Converted text to UPPERCASE[/EN][PT]Texto convertido para MAIÚSCULAS[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]