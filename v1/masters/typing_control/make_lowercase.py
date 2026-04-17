import pyautogui
import pyperclip
import time

def execute(arguments: dict, context: dict) -> str:
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)
    text = pyperclip.paste()
    pyperclip.copy(text.lower())
    pyautogui.hotkey('ctrl', 'v')
    return '[DIRECT][EN]Converted text to lowercase[/EN][PT]Texto convertido para minúsculas[/PT]'

REQUIREMENTS = ["pyautogui", "pyperclip"]