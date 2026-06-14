async def execute(arguments: dict, context: dict) -> str:
    if not hasattr(context['config'], '_browser_instance'):
        return '[DIRECT][EN]No browser open[/EN][PT]Nenhum navegador aberto[/PT]'
    
    page = context['config']._browser_instance['page']
    description = arguments.get('description', '').lower()
    
    if not description:
        return '[DIRECT][EN]Error: description required[/EN][PT]Erro: descrição obrigatória[/PT]'
    
    try:
        # Common element patterns
        patterns = {
            'search': ['input[name*="search"]', 'input[type="search"]', 'input[placeholder*="search"]', '[aria-label*="search"]'],
            'login': ['button:has-text("login")', 'button:has-text("sign in")', 'a:has-text("login")'],
            'submit': ['button[type="submit"]', 'input[type="submit"]', 'button:has-text("submit")'],
            'menu': ['button[aria-label*="menu"]', '[role="button"]:has-text("menu")'],
            'close': ['button[aria-label*="close"]', 'button:has-text("×")', '[aria-label*="close"]'],
        }
        
        # Try pattern matching first
        selectors = []
        for key, pattern_list in patterns.items():
            if key in description:
                selectors.extend(pattern_list)
        
        # Fallback: try text matching
        if not selectors:
            selectors = [
                f'button:has-text("{description}")',
                f'a:has-text("{description}")',
                f'input[placeholder*="{description}"]',
                f'[aria-label*="{description}"]'
            ]
        
        # Try each selector
        for selector in selectors:
            try:
                await page.click(selector, timeout=2000)
                return f'[DIRECT][EN]Clicked on: {description}[/EN][PT]Clicado em: {description}[/PT]'
            except:
                continue
        
        return f'[DIRECT][EN]Could not find: {description}[/EN][PT]Não encontrado: {description}[/PT]'
    
    except Exception as e:
        return f'[DIRECT][EN]Click error: {str(e)}[/EN][PT]Erro ao clicar: {str(e)}[/PT]'

REQUIREMENTS = ['playwright']