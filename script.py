import re

with open('slides.md', 'r', encoding='utf-8') as f:
    text = f.read()

def repl(m):
    num = int(m.group(1))
    if num >= 6:
        return f'<SlideNum num="{num+1:02d}" />'
    return m.group(0)

new_text = re.sub(r'<SlideNum num="(\d+)" />', repl, text)

with open('slides.md', 'w', encoding='utf-8') as f:
    f.write(new_text)
print('Done!')
