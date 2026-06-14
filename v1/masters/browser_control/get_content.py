async def execute(arguments: dict, context: dict) -> str:
    if not hasattr(context['config'], '_browser_instance'):
        return '[DIRECT][EN]No browser open[/EN][PT]Nenhum navegador aberto[/PT]'
    
    page = context['config']._browser_instance['page']
    
    try:
        # Get visible text content
        content = await page.evaluate('''() => {
            const walker = document.createTreeWalker(
                document.body,
                NodeFilter.SHOW_TEXT,
                {
                    acceptNode: function(node) {
                        const parent = node.parentElement;
                        if (!parent) return NodeFilter.FILTER_REJECT;
                        
                        const style = window.getComputedStyle(parent);
                        if (style.display === 'none' || style.visibility === 'hidden') {
                            return NodeFilter.FILTER_REJECT;
                        }
                        
                        const text = node.textContent.trim();
                        if (text.length === 0) return NodeFilter.FILTER_REJECT;
                        
                        return NodeFilter.FILTER_ACCEPT;
                    }
                }
            );
            
            const texts = [];
            let node;
            while (node = walker.nextNode()) {
                texts.push(node.textContent.trim());
            }
            
            return texts.join(' ');
        }''')
        
        # Limit size
        if len(content) > 4000:
            content = content[:4000] + '... (truncated)'
        
        return f'[SYSTEM]Page content:\n{content}[/SYSTEM]'
    
    except Exception as e:
        return f'[DIRECT][EN]Error: {str(e)}[/EN][PT]Erro: {str(e)}[/PT]'

REQUIREMENTS = ['playwright']