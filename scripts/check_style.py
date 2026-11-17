from pathlib import Path
import re
import sys

errors = []
for path in sorted(Path('docs').rglob('*.md')):
    text = path.read_text(encoding='utf-8')
    for n, line in enumerate(text.splitlines(), 1):
        if any(chr(code) in line for code in [0x2014, 0x2013, 0xAB, 0xBB, 0x201C, 0x201D, 0xF7]):
            errors.append(f'{path}:{n}: forbidden punctuation')
    if len(re.findall(r'^# ', text, re.M)) != 1:
        errors.append(f'{path}: expected one H1')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Style checks passed')
