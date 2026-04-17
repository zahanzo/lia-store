"""
Browser State - Comunicação com navegador Playwright via subprocesso persistente.
"""

import os
import json
import subprocess
import sys
import time
import tempfile
import atexit

_server_process = None
_command_dir = None
_command_counter = 0

def _get_command_dir():
    global _command_dir
    if _command_dir is None:
        _command_dir = tempfile.mkdtemp(prefix="browser_control_")
        atexit.register(_cleanup_command_dir)
    return _command_dir

def _cleanup_command_dir():
    global _command_dir
    if _command_dir and os.path.exists(_command_dir):
        import shutil
        shutil.rmtree(_command_dir, ignore_errors=True)

def _ensure_server():
    """Garante que o servidor Playwright está rodando."""
    global _server_process
    if _server_process is not None and _server_process.poll() is None:
        return  # já está rodando

    # Cria script do servidor
    server_script = os.path.join(_get_command_dir(), "browser_server.py")
    with open(server_script, "w", encoding="utf-8") as f:
        f.write("""
import sys
import json
import time
import os
from playwright.sync_api import sync_playwright

def main():
    cmd_dir = sys.argv[1]
    playwright = None
    browser = None
    page = None

    print("[SERVER] Playwright server started.", flush=True)

    while True:
        # Procura por arquivos de comando
        for filename in os.listdir(cmd_dir):
            if not filename.startswith("cmd_"):
                continue
            cmd_path = os.path.join(cmd_dir, filename)
            res_path = cmd_path.replace("cmd_", "res_")

            try:
                with open(cmd_path, "r", encoding="utf-8") as f:
                    cmd = json.load(f)

                action = cmd.get("action")
                args = cmd.get("args", {})
                result = {"status": "ok", "data": None}

                if action == "ping":
                    result["data"] = "pong"
                elif action == "launch":
                    if not playwright:
                        playwright = sync_playwright().start()
                        browser = playwright.firefox.launch(headless=False)
                        page = browser.new_page()
                    result["data"] = "Browser launched"
                elif action == "navigate":
                    if page:
                        page.goto(args["url"], timeout=30000)
                        result["data"] = f"Navigated to {args['url']}"
                    else:
                        result = {"status": "error", "message": "No page"}
                elif action == "snapshot":
                    if page:
                        elements = page.evaluate('''() => {
                            const selectors = ['button', 'a', 'input[type="submit"]', 'input[type="button"]', '[role="button"]', '[onclick]'];
                            const results = [];
                            const seen = new Set();
                            selectors.forEach(sel => {
                                document.querySelectorAll(sel).forEach(el => {
                                    if (seen.has(el)) return;
                                    seen.add(el);
                                    const text = (el.innerText || el.value || el.getAttribute('aria-label') || el.getAttribute('title') || '').trim();
                                    if (text && text.length < 200) {
                                        const tag = el.tagName.toLowerCase();
                                        const id = el.id ? '#' + el.id : '';
                                        const classes = el.className ? '.' + el.className.split(' ').join('.') : '';
                                        results.push({text: text, selector: tag + id + classes});
                                    }
                                });
                            });
                            return results.slice(0, 30);
                        }''')
                        result["data"] = elements
                    else:
                        result = {"status": "error", "message": "No page"}
                elif action == "click_text":
                    if page:
                        page.get_by_text(args["text"], exact=True).click()
                        result["data"] = f"Clicked '{args['text']}'"
                    else:
                        result = {"status": "error", "message": "No page"}
                elif action == "click_selector":
                    if page:
                        page.click(args["selector"])
                        result["data"] = f"Clicked '{args['selector']}'"
                    else:
                        result = {"status": "error", "message": "No page"}
                elif action == "type_label":
                    if page:
                        page.get_by_label(args["label"]).fill(args["text"])
                        if args.get("press_enter"):
                            page.keyboard.press("Enter")
                        result["data"] = f"Typed '{args['text']}' into {args['label']}"
                    else:
                        result = {"status": "error", "message": "No page"}
                elif action == "type_selector":
                    if page:
                        page.fill(args["selector"], args["text"])
                        if args.get("press_enter"):
                            page.keyboard.press("Enter")
                        result["data"] = f"Typed '{args['text']}' into {args['selector']}"
                    else:
                        result = {"status": "error", "message": "No page"}
                elif action == "scroll":
                    if page:
                        delta = args.get("amount", 500)
                        if args.get("direction") == "up":
                            delta = -delta
                        page.evaluate(f"window.scrollBy(0, {delta})")
                        result["data"] = f"Scrolled {args.get('direction', 'down')}"
                    else:
                        result = {"status": "error", "message": "No page"}
                elif action == "back":
                    if page:
                        page.go_back()
                        result["data"] = "Went back"
                    else:
                        result = {"status": "error", "message": "No page"}
                elif action == "forward":
                    if page:
                        page.go_forward()
                        result["data"] = "Went forward"
                    else:
                        result = {"status": "error", "message": "No page"}
                elif action == "refresh":
                    if page:
                        page.reload()
                        result["data"] = "Page refreshed"
                    else:
                        result = {"status": "error", "message": "No page"}
                elif action == "get_text":
                    if page:
                        selector = args.get("selector", "body")
                        text = page.text_content(selector)
                        result["data"] = text[:1000]
                    else:
                        result = {"status": "error", "message": "No page"}
                elif action == "screenshot":
                    if page:
                        page.screenshot(path=args["path"])
                        result["data"] = f"Screenshot saved to {args['path']}"
                    else:
                        result = {"status": "error", "message": "No page"}
                elif action == "press_key":
                    if page:
                        page.keyboard.press(args["key"])
                        result["data"] = f"Pressed {args['key']}"
                    else:
                        result = {"status": "error", "message": "No page"}
                elif action == "close":
                    if browser:
                        browser.close()
                        playwright.stop()
                    result["data"] = "Browser closed"
                    playwright = None
                    browser = None
                    page = None
                elif action == "shutdown":
                    if browser:
                        browser.close()
                        playwright.stop()
                    result["data"] = "Server shutting down"
                    with open(res_path, "w") as f:
                        json.dump(result, f)
                    os.remove(cmd_path)
                    sys.exit(0)
                else:
                    result = {"status": "error", "message": f"Unknown action: {action}"}

                with open(res_path, "w") as f:
                    json.dump(result, f)
                os.remove(cmd_path)

            except Exception as e:
                result = {"status": "error", "message": str(e)}
                with open(res_path, "w") as f:
                    json.dump(result, f)
                try:
                    os.remove(cmd_path)
                except:
                    pass

        time.sleep(0.1)

if __name__ == "__main__":
    main()
""")

    # Inicia o subprocesso
    _server_process = subprocess.Popen(
        [sys.executable, server_script, _get_command_dir()],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    # Aguarda inicialização
    time.sleep(1.0)
    # Garante que o navegador seja lançado
    _send_command("launch", {})

def _send_command(action, args, timeout=30):
    """Envia comando ao servidor e aguarda resposta."""
    global _command_counter
    _ensure_server()

    _command_counter += 1
    cmd_file = os.path.join(_get_command_dir(), f"cmd_{_command_counter}.json")
    res_file = os.path.join(_get_command_dir(), f"res_{_command_counter}.json")

    with open(cmd_file, "w") as f:
        json.dump({"action": action, "args": args}, f)

    # Aguarda resposta
    start = time.time()
    while not os.path.exists(res_file):
        if time.time() - start > timeout:
            raise TimeoutError(f"Timeout waiting for response to {action}")
        time.sleep(0.05)

    with open(res_file, "r") as f:
        result = json.load(f)

    os.remove(res_file)
    if result.get("status") == "error":
        raise Exception(result.get("message", "Unknown error"))
    return result.get("data")