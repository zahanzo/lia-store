"""
Direct Search Plugin
Opens a URL or Google search DIRECTLY in the physical browser for the user to see.
"""

import webbrowser
import pywhatkit

def execute(arguments: dict, context: dict) -> str:
    query = arguments.get("query", "").strip()
    if not query:
        return "[DIRECT][EN]Please provide a query or URL.[/EN][PT]Forneça uma consulta ou URL.[/PT]"
    
    if query.startswith("http") or "www." in query or ".com" in query:
        url = query if query.startswith("http") else f"https://{query}"
        webbrowser.open(url)
        return f"[DIRECT][EN]I've opened the link {url} in your browser, love![/EN][PT]Já abri o link {url} no seu navegador, vida![/PT]"
    else:
        pywhatkit.search(query)
        return f"[DIRECT][EN]I opened the search for '{query}' in your browser, love.[/EN][PT]Abri a pesquisa sobre '{query}' no seu navegador, amor.[/PT]"

REQUIREMENTS = ["webbrowser", "pywhatkit"]