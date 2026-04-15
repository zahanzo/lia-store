"""
Web Search Plugin
Searches the internet using DuckDuckGo (ddgs library)
"""

def execute(arguments: dict, context: dict) -> str:
    """
    Execute the web search tool.
    
    Args:
        arguments: Tool arguments from AI (e.g., {"query": "..."})
        context: Execution context (db connection, etc.)
    
    Returns:
        AI response string with [DIRECT] tag for fast-track
    """
    query = arguments.get("query", "").strip()
    
    if not query:
        return "[DIRECT][EN]Please provide a search query.[/EN][PT]Por favor forneça uma consulta de busca.[/PT]"
    
    print(f"🕵️ [Search] Searching for: '{query}'...", flush=True)
    
    # Try with new ddgs library
    try:
        from ddgs import DDGS
        
        with DDGS() as ddgs_instance:
            results = list(ddgs_instance.text(
                query, 
                region='wt-wt',  # Worldwide
                safesearch='moderate',
                max_results=5
            ))
        
        if results:
            print(f"✅ [Search] Found {len(results)} results", flush=True)
            
            # Format results
            formatted_text = "Search results:\n\n"
            for i, r in enumerate(results, 1):
                title = r.get('title', 'No title')
                body = r.get('body', 'No description')
                href = r.get('href', '')
                formatted_text += f"[{i}] {title}\nSummary: {body}\nLink: {href}\n\n"
            
            return formatted_text
        else:
            print("⚠️ [Search] No results from primary search", flush=True)
    
    except ImportError:
        print("⚠️ [Search] ddgs library not installed, using fallback", flush=True)
    except Exception as e:
        print(f"⚠️ [Search] Primary search error: {e}", flush=True)
    
    # Fallback: Use requests to DuckDuckGo Lite
    try:
        import requests
        from html.parser import HTMLParser
        
        # Use DuckDuckGo Lite HTML version as backup
        url = f"https://lite.duckduckgo.com/lite/?q={query.replace(' ', '+')}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            # Simple parsing of DuckDuckGo Lite results
            class DDGParser(HTMLParser):
                def __init__(self):
                    super().__init__()
                    self.results = []
                    self.current_result = {}
                    self.in_link = False
                    self.in_snippet = False
                    self.link_text = ""
                    self.snippet_text = ""
                    
                def handle_starttag(self, tag, attrs):
                    attrs_dict = dict(attrs)
                    if tag == 'a':
                        # Check if it's a result link (has href that's not internal)
                        href = attrs_dict.get('href', '')
                        if href and not href.startswith('/') and not 'duckduckgo' in href:
                            self.in_link = True
                            self.current_result = {'href': href}
                            self.link_text = ""
                    elif tag == 'td':
                        # Result snippets are in <td> tags
                        class_name = attrs_dict.get('class', '')
                        if 'result-snippet' in class_name:
                            self.in_snippet = True
                            self.snippet_text = ""
                
                def handle_data(self, data):
                    if self.in_link:
                        self.link_text += data.strip() + " "
                    elif self.in_snippet:
                        self.snippet_text += data.strip() + " "
                
                def handle_endtag(self, tag):
                    if tag == 'a' and self.in_link:
                        self.in_link = False
                        if self.link_text.strip():
                            self.current_result['title'] = self.link_text.strip()
                    elif tag == 'td' and self.in_snippet:
                        self.in_snippet = False
                        if self.snippet_text.strip():
                            self.current_result['body'] = self.snippet_text.strip()
                            if 'title' in self.current_result:
                                self.results.append(self.current_result.copy())
                                self.current_result = {}
            
            parser = DDGParser()
            parser.feed(response.text)
            
            if parser.results:
                print(f"✅ [Search] Found {len(parser.results)} results (fallback)", flush=True)
                
                formatted_text = "Search results:\n\n"
                for i, r in enumerate(parser.results[:5], 1):
                    formatted_text += f"[{i}] {r.get('title', 'No title')}\n"
                    formatted_text += f"Summary: {r.get('body', 'No description')}\n"
                    formatted_text += f"Link: {r.get('href', '')}\n\n"
                
                return formatted_text
    
    except Exception as e:
        print(f"⚠️ [Search] Fallback error: {e}", flush=True)
    
    # If everything fails
    return f"[DIRECT][EN]I had trouble searching for '{query}'. The search engine might be temporarily unavailable. Try again in a moment.[/EN][PT]Tive problemas ao buscar por '{query}'. O buscador pode estar temporariamente indisponível. Tente novamente em um momento.[/PT]"


REQUIREMENTS = ["ddgs", "requests"]