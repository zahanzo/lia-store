async def execute(arguments: dict, context: dict) -> str:
    if not hasattr(context['config'], '_browser_instance'):
        return '[DIRECT][EN]No browser open[/EN][PT]Nenhum navegador aberto[/PT]'
    
    page = context['config']._browser_instance['page']
    description = arguments.get('description', '').lower()
    text = arguments.get('text', '')
    
    if not text:
        return '[DIRECT][EN]Error: text required[/EN][PT]Erro: texto obrigatório[/PT]'
    
    try:
        # Common input patterns
        patterns = {
            'search': ['input[name*="search"]', 'input[type="search"]', 'input[placeholder*="search"]'],
            'email': ['input[type="email"]', 'input[name*="email"]'],
            'password': ['input[type="password"]', 'input[name*="password"]'],
            'username': ['input[name*="user"]', 'input[name*="login"]'],
            'name': ['input[name*="name"]', 'input[placeholder*="name"]'],
        }
        
        # Try pattern matching
        selectors = []
        if description:
            for key, pattern_list in patterns.items():
                if key in description:
                    selectors.extend(pattern_list)
        
        # Fallback: generic inputs
        if not selectors:
            selectors = [
                'input[type="text"]',
                'input:not([type])',
                'textarea',
                f'input[placeholder*="{description}"]' if description else None
            ]
            selectors = [s for s in selectors if s]
        
        # Try each selector
        for selector in selectors:
            try:
                await page.fill(selector, text, timeout=2000)
                return f'[DIRECT][EN]Typed: {text}[/EN][PT]Digitado: {text}[/PT]'
            except:
                continue
        
        return f'[DIRECT][EN]Could not find input[/EN][PT]Input não encontrado[/PT]'
    
    except Exception as e:
        return f'[DIRECT][EN]Type error: {str(e)}[/EN][PT]Erro ao digitar: {str(e)}[/PT]'

REQUIREMENTS = ['playwright']