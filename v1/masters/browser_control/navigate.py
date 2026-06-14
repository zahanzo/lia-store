async def execute(arguments: dict, context: dict) -> str:
    from playwright.async_api import async_playwright
    
    url = arguments.get('url', '')
    if not url:
        return '[DIRECT][EN]Error: URL required[/EN][PT]Erro: URL obrigatória[/PT]'
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Get or create browser instance
    if not hasattr(context['config'], '_browser_instance'):
        pw = await async_playwright().start()
        browser = await pw.firefox.launch(headless=False)
        page = await browser.new_page()
        context['config']._browser_instance = {'pw': pw, 'browser': browser, 'page': page}
    
    page = context['config']._browser_instance['page']
    
    try:
        await page.goto(url, wait_until='domcontentloaded', timeout=30000)
        title = await page.title()
        return f'[DIRECT][EN]Navigated to: {title}[/EN][PT]Navegado para: {title}[/PT]'
    except Exception as e:
        return f'[DIRECT][EN]Error: {str(e)}[/EN][PT]Erro: {str(e)}[/PT]'

REQUIREMENTS = ['playwright']