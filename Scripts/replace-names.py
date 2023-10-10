# Автозамена имён и названий в английских субтитрах

from os import listdir
from os.path import isfile, join, realpath, dirname
import re

src_dir = realpath(join(dirname(__file__), '..', '1-English'))

# Сюда дописываем новые замены
name_fixes = {
    'Adley':        'Ardley',
    'Blanny':       'Frannie',
    'Kurin':        'Clint',
    'Kurrin':       'Clint',
    'forrest':      'forest',
}

class Replacement:
    def __init__(self, old: str, new: str):
        self.old = old
        self.new = new
        self.pattern = re.compile(r'\b' + old + r'\b')
        self.count = 0

    def __str__(self) -> str:
        return self.old + ' -> ' + self.new + ': ' + str(self.count)


replacements = [Replacement(old, new) for (old, new) in name_fixes.items()]

def replace_all(s: str) -> str:
    for r in replacements:
        s, count = re.subn(r.pattern, r.new, s)
        r.count += count

    return s

file_names = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]
for name in file_names:
    print(name, '...')
    out_lines = []
    with open(join(src_dir, name), 'rt') as inf:
        out_lines = [replace_all(line) for line in inf.readlines()]
    
    with open(join(src_dir, name), 'wt') as outf:
        outf.writelines(out_lines)

print('Replacements made:')
for r in replacements:
    print(r)
