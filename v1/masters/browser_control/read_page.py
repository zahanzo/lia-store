async def execute(arguments: dict, context: dict) -> str:
    if not hasattr(context['config'], '_browser_instance'):
        return '[DIRECT][EN]No browser open[/EN][PT]Nenhum navegador aberto[/PT]'
    
    page = context['config']._browser_instance['page']
    
    try:
        # Get accessibility snapshot
        snapshot = await page.accessibility.snapshot()
        
        def format_tree(node, depth=0):
            if not node:
                return ""
            
            indent = "  " * depth
            name = node.get('name', '')
            role = node.get('role', '')
            
            # Only show interactive/important elements
            important_roles = ['button', 'link', 'textbox', 'searchbox', 'heading', 
                             'input', 'checkbox', 'radio', 'combobox', 'tab', 'menuitem']
            
            lines = []
            if role in important_roles or name:
                desc = f"{indent}- {role}"
                if name:
                    desc += f': "{name}"'
                lines.append(desc)
            
            # Recurse children
            for child in node.get('children', []):
                lines.append(format_tree(child, depth + 1))
            
            return '\n'.join(filter(None, lines))
        
        tree = format_tree(snapshot)
        
        # Limit size
        if len(tree) > 3000:
            tree = tree[:3000] + "\n... (truncated)"
        
        return f'[SYSTEM]Page structure:\n{tree}[/SYSTEM]'
    except Exception as e:
        return f'[DIRECT][EN]Error reading page: {str(e)}[/EN][PT]Erro ao ler página: {str(e)}[/PT]'

REQUIREMENTS = ['playwright']