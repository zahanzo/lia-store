"""
Test Code Plugin
Reads the last code saved in the database and executes it in the terminal to validate errors.
"""

import os
import json
import subprocess

def execute(arguments: dict, context: dict) -> str:
    run_db = context.get("run_db")
    
    path_to_test = None
    result = run_db("SELECT valor_texto FROM system_state WHERE chave = 'last_action'")
    if result and result[0][0]:
        try:
            parsed = json.loads(result[0][0])
            path_to_test = parsed.get("last_file", parsed.get("ultimo_arquivo"))
        except:
            pass
    
    if not path_to_test or not os.path.exists(path_to_test):
        return "[DIRECT][EN]I couldn't find any recent code to test, love.[/EN][PT]Não encontrei nenhum código recente para testar, amor.[/PT]"
    
    if path_to_test.endswith(".py"):
        command = ['python', path_to_test]
    elif path_to_test.endswith(".js"):
        command = ['node', path_to_test]
    else:
        return "[DIRECT][EN]I don't know how to automatically test files of this language yet.[/EN][PT]Eu ainda não sei como testar arquivos dessa linguagem automaticamente.[/PT]"
    
    try:
        process = subprocess.run(command, input="2000\n", capture_output=True, text=True, timeout=5)
        log_path = path_to_test.rsplit('.', 1)[0] + "_log.txt"
        log_content = f"--- TEST RESULT ---\nStatus: {'✅ SUCCESS' if process.returncode == 0 else '❌ ERROR'}\n\nSTDOUT:\n{process.stdout}\n\nSTDERR:\n{process.stderr}"
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(log_content)
        
        if process.returncode == 0:
            return "[DIRECT][EN]The code ran perfectly, love! I've left the success log on your Desktop.[/EN][PT]O código rodou perfeitamente, vida! Já deixei o log de sucesso no seu Desktop.[/PT]"
        else:
            return "[DIRECT][EN]The test showed some errors. Take a look at the log I saved on your Desktop.[/EN][PT]O teste apontou alguns erros. Dá uma olhadinha no log que eu salvei na sua Área de Trabalho.[/PT]"
    except subprocess.TimeoutExpired:
        return "[DIRECT][EN]The test took too long and I had to stop it. There might be an infinite loop there![/EN][PT]O teste demorou demais e eu precisei interromper. Pode ter um loop infinito aí![/PT]"
    except Exception as e:
        return f"[DIRECT][EN]I had a technical problem trying to run the test: {e}[/EN][PT]Tive um problema técnico ao tentar rodar o teste: {e}[/PT]"

REQUIREMENTS = []