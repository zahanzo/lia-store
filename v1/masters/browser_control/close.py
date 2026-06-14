async def execute(arguments: dict, context: dict) -> str:
    if not hasattr(context['config'], '_browser_instance'):
        return '[DIRECT][EN]No browser open[/EN][PT]Nenhum navegador aberto[/PT]'
    
    instance = context['config']._browser_instance
    
    try:
        await instance['browser'].close()
        await instance['pw'].stop()
        delattr(context['config'], '_browser_instance')
        return '[DIRECT][EN]Browser closed[/EN][PT]Navegador fechado[/PT]'
    except Exception as e:
        return f'[DIRECT][EN]Close error: {str(e)}[/EN][PT]Erro ao fechar: {str(e)}[/PT]'

REQUIREMENTS = ['playwright']