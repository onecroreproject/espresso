import os
import re

directory = r'c:\Agathiyan\Espresso_BW\templates'

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find all CSS blocks
            def replace_in_block(match):
                block = match.group(0)
                # If the block has a var(--accent) background and var(--text-primary) text color
                if re.search(r'background(?:-color)?:\s*var\(--accent\)', block) and re.search(r'color:\s*var\(--text-primary\)', block):
                    block = re.sub(r'color:\s*var\(--text-primary\)', 'color: #000000', block)
                return block

            content = re.sub(r'\{[^{}]*\}', replace_in_block, content)

            # Also fix inline styles
            def replace_inline(match):
                inline = match.group(0)
                if re.search(r'background(?:-color)?:\s*var\(--accent\)', inline) and re.search(r'color:\s*var\(--text-primary\)', inline):
                    inline = re.sub(r'color:\s*var\(--text-primary\)', 'color: #000000', inline)
                return inline
                
            content = re.sub(r'style=\'[^\']*\'|style=\"[^\"]*\"', replace_inline, content)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
print('Done fixing colors to black!')