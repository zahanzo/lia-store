async def execute(arguments: dict, context: dict) -> str:
    if not hasattr(context['config'], '_browser_instance'):
        return '[DIRECT][EN]No browser open[/EN][PT]Nenhum navegador aberto[/PT]'
    
    page = context['config']._browser_instance['page']
    direction = arguments.get('direction', 'down').lower()
    
    try:
        if direction in ['down', 'baixo']:
            await page.evaluate('window.scrollBy(0, window.innerHeight)')
            return '[DIRECT][EN]Scrolled down[/EN][PT]Rolou para baixo[/PT]'
        elif direction in ['up', 'cima']:
            await page.evaluate('window.scrollBy(0, -window.innerHeight)')
            return '[DIRECT][EN]Scrolled up[/EN][PT]Rolou para cima[/PT]'
        elif direction in ['top', 'topo']:
            await page.evaluate('window.scrollTo(0, 0)')
            return '[DIRECT][EN]Scrolled to top[/EN][PT]Rolou para o topo[/PT]'
        elif direction in ['bottom', 'fim']:
            await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            return '[DIRECT][EN]Scrolled to bottom[/EN][PT]Rolou para o fim[/PT]'
        else:
            return '[DIRECT][EN]Invalid direction[/EN][PT]Direção inválida[/PT]'
    
    except Exception as e:
        return f'[DIRECT][EN]Scroll error: {str(e)}[/EN][PT]Erro ao rolar: {str(e)}[/PT]'

REQUIREMENTS = ['playwright']