async def execute(arguments: dict, context: dict) -> str:
    import os
    from pathlib import Path
    from datetime import datetime
    
    if not hasattr(context['config'], '_browser_instance'):
        return '[DIRECT][EN]No browser open[/EN][PT]Nenhum navegador aberto[/PT]'
    
    page = context['config']._browser_instance['page']
    
    try:
        # Create screenshots directory
        screenshots_dir = Path(os.path.dirname(__file__)).parent.parent / 'data' / 'screenshots'
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'screenshot_{timestamp}.png'
        filepath = screenshots_dir / filename
        
        await page.screenshot(path=str(filepath), full_page=False)
        
        return f'[DIRECT][EN]Screenshot saved: {filename}[/EN][PT]Screenshot salvo: {filename}[/PT]'
    except Exception as e:
        return f'[DIRECT][EN]Screenshot error: {str(e)}[/EN][PT]Erro: {str(e)}[/PT]'

REQUIREMENTS = ['playwright']