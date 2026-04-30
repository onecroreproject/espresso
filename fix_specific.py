import os
import re

files_to_check = ['payment.html', 'help.html', 'change_password.html', 'order.html']
directory = r'c:\Agathiyan\Espresso_BW\templates'

for filename in files_to_check:
    path = os.path.join(directory, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        def replace_in_block(match):
            block = match.group(0)
            if re.search(r'background(?:-color)?:\s*(?:var\(--accent\)|#FFDEAD|#ffdead)', block):
                if re.search(r'color:\s*(?:var\(--text-primary\)|white|#fff|#ffffff|#FFF|#FFFFFF|#000|#000000)\s*;', block):
                    block = re.sub(r'color:\s*(?:var\(--text-primary\)|white|#fff|#ffffff|#FFF|#FFFFFF)\s*;', 'color: #000000;', block)
            return block
            
        content = re.sub(r'\{[^{}]*\}', replace_in_block, content)
        
        # fix inline styles
        def replace_inline(match):
            inline = match.group(0)
            if re.search(r'background(?:-color)?:\s*(?:var\(--accent\)|#FFDEAD|#ffdead)', inline):
                if re.search(r'color:\s*(?:var\(--text-primary\)|white|#fff|#ffffff|#FFF|#FFFFFF|#000|#000000)\s*;?', inline):
                    inline = re.sub(r'color:\s*(?:var\(--text-primary\)|white|#fff|#ffffff|#FFF|#FFFFFF)\s*;?', 'color:#000000;', inline)
            return inline
            
        content = re.sub(r'style=\'[^\']*\'|style=\"[^\"]*\"', replace_inline, content)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
print('Done fixing specific files!')